import requests

# 設定資料來源 URL
url = 'https://data.moenv.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate desc&format=JSON'

# 發送 GET 請求來取得 JSON 資料
response = requests.get(url)

# 檢查請求是否成功
if response.status_code == 200:
    data = response.json()  # 將回應的內容轉為 JSON 格式
    records = data['records']  # 取得記錄資料

    # 顯示總筆數
    print(f"資料總筆數: {len(records)}")

    # 顯示每筆資料的內容
    print("臺灣各地AQI")
    for item in records:
        print(f"城市: {item['county']}, 地點: {item['sitename']}, AQI: {item['aqi']}, 狀態: {item['status']}")
        print(f"so2: {item['so2']}, co: {item['co']}, o3: {item['o3']}, no2: {item['no2']}, nox: {item['nox']}, no: {item['no']}, pm2.5: {item['pm2.5']}")
        print()  # 換行分隔
else:
    # 顯示錯誤訊息
    print(f"無法取得資料, 錯誤代碼: {response.status_code}")
