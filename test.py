from vsce_downloads import get_extension_stats, print_stats

# 方式1：格式化打印
print_stats("knighthood2001.urdf-formatting")

# 方式2：获取字典自行处理
data = get_extension_stats("knighthood2001.urdf-formatting")
print(data)
print(data["vscode_download"], data["vsix_download"])
