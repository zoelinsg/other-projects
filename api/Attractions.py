import requests
import json

# 設定資料來源 URL
url = 'https://media.taiwan.net.tw/XMLReleaseALL_public/scenic_spot_C_f.json'

# 發送 GET 請求來取得 JSON 資料
response = requests.get(url)

# 檢查請求是否成功
if response.status_code == 200:
    # 將回應的內容解析成 JSON
    data = response.json()

    # 顯示 JSON 資料的部分內容 (例如前幾個景點)
    for item in data['XML_Head']['Infos']['Info'][:3]:
        print(f"景點名稱: {item['Name']}")
        print(f"地址: {item['Add']}")
        print(f"描述: {item['Description']}")
        print()
else:
    print(f"無法取得資料, 錯誤代碼: {response.status_code}")