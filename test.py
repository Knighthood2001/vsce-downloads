import requests

url = "https://marketplace.visualstudio.com/_apis/public/gallery/extensionquery?api-version=7.2-preview.1"

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
}

payload = {
    "filters": [
        {
            "criteria": [
                {
                    "filterType": 7,
                    "value": "knighthood2001.ros2-quick-runner"
                }
            ],
            "pageNumber": 1,
            "pageSize": 1
        }
    ],
    "flags": 1792
}

resp = requests.post(url, json=payload)
data = resp.json()

ext = data["results"][0]["extensions"][0]
stats = ext["statistics"]

res = {}
for item in stats:
    res[item["statisticName"]] = item["value"]

print("==== VSCode 插件统计信息 ====")
print(f"总安装量：{int(res['install'])}")
print(f"VSIX网页下载次数：{int(res['downloadCount'])}")
print(f"总更新次数：{int(res['updateCount'])}")
# print(f"平均评分：{res['averagerating']}")
# print(f"评分人数：{int(res['ratingcount'])}")
print(f"当日新增安装：{res['trendingdaily']}")
print(f"周日均新增：{res['trendingweekly']:.2f}")
print(f"月日均新增：{res['trendingmonthly']:.2f}")
