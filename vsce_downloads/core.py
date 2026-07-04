import requests

API_URL = "https://marketplace.visualstudio.com/_apis/public/gallery/extensionquery?api-version=7.2-preview.1"
HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
}
REQUEST_TIMEOUT = 15


def get_extension_stats(extension_id: str) -> dict:
    """
    获取 VSCode 扩展市场统计数据
    :param extension_id: 插件ID，格式 publisher.extension-name
    :return: 统计结果字典
    """
    payload = {
        "filters": [
            {
                "criteria": [
                    {
                        "filterType": 7,
                        "value": extension_id
                    }
                ],
                "pageNumber": 1,
                "pageSize": 1
            }
        ],
        "flags": 1792
    }

    resp = requests.post(API_URL, json=payload, headers=HEADERS, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    data = resp.json()

    try:
        ext = data["results"][0]["extensions"][0]
    except (KeyError, IndexError) as exc:
        raise ValueError(f"Extension not found: {extension_id}") from exc

    stats = ext["statistics"]

    res = {}
    for item in stats:
        res[item["statisticName"]] = item["value"]

    # 各渠道下载量
    vscode_download = int(res["install"]) if "install" in res else 0
    vsix_download = int(res["downloadCount"]) if "downloadCount" in res else 0

    result = {
        "vscode_download": vscode_download,
        "vsix_download": vsix_download,
        "total_install": vscode_download + vsix_download,  # 总安装量 = 两者之和
        "update_count": int(res["updateCount"]) if "updateCount" in res else 0,
        "trending_daily": res.get("trendingdaily", 0.0),
        "trending_weekly": res.get("trendingweekly", 0.0),
        "trending_monthly": res.get("trendingmonthly", 0.0)
    }

    # 平均评分、评分人数异常兜底
    try:
        result["average_rating"] = res["averagerating"]
    except (KeyError, TypeError):
        result["average_rating"] = None

    try:
        result["rating_count"] = int(res["ratingcount"])
    except (KeyError, TypeError):
        result["rating_count"] = None

    return result


def print_stats(ext_id: str):
    """格式化打印统计信息"""
    stat = get_extension_stats(ext_id)
    print("==== VSCode 插件统计信息 ====")
    print(f"插件名称：{ext_id}")
    print(f"总安装量：{stat['total_install']}")
    print(f"VSCode 编辑器内下载量：{stat['vscode_download']}")
    print(f"VSIX 离线包网页下载量：{stat['vsix_download']}")
    print(f"总更新次数：{stat['update_count']}")

    if stat["average_rating"] is not None:
        print(f"平均评分：{stat['average_rating']}")
    else:
        print("平均评分：暂无评分")

    if stat["rating_count"] is not None:
        print(f"评分人数：{stat['rating_count']}")
    else:
        print("评分人数：暂无评分")

    print(f"当日新增安装：{stat['trending_daily']}")
    print(f"周日均新增：{stat['trending_weekly']:.2f}")
    print(f"月日均新增：{stat['trending_monthly']:.2f}")


if __name__ == "__main__":
    # 测试入口
    print_stats("knighthood2001.ros2-quick-runner")
