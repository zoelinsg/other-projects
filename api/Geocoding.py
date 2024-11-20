import requests  # 導入 requests 庫來發送 HTTP 請求

# API 基本 URL (使用 HTTPS)
base_url = "https://api.openweathermap.org/geo/1.0/reverse"

def get_geocoding_data(lat, lon, limit, api_key):
    """
    發送請求至 OpenWeatherMap API 並返回地理編碼數據.
    
    :param lat: 經度
    :param lon: 緯度
    :param limit: 返回的結果數量限制
    :param api_key: API 金鑰
    :return: JSON 格式的地理編碼數據或 None (如有錯誤)
    """
    # 構建正確的 API 請求 URL
    url = f"{base_url}?lat={lat}&lon={lon}&limit={limit}&appid={api_key}"
    try:
        response = requests.get(url)  # 發送 GET 請求
        response.raise_for_status()  # 檢查請求是否成功
        return response.json()  # 解析回應的 JSON 數據
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP 錯誤: {http_err}")  # 打印 HTTP 錯誤訊息
    except Exception as err:
        print(f"其他錯誤: {err}")  # 打印其他錯誤
    return None

def display_geocoding_info(geocoding_data):
    """
    顯示地理編碼數據.
    
    :param geocoding_data: API 返回的地理編碼數據
    """
    if geocoding_data:
        # 遍歷數據列表中的每個預測
        for forecast in geocoding_data:
            name = forecast['name']  # 城市名稱
            lat = forecast['lat']  # 經度
            lon = forecast['lon']  # 緯度
            
            print(f"城市: {name}")
            print(f"緯度: {lat}")
            print(f"經度: {lon}")
            print("-" * 30)  # 分隔線讓輸出更清晰
    else:
        print("無法顯示數據，請檢查 API 回應.")

# 您的 API 金鑰
api_key = "ad09566d2f0f34027d4b7070d3d73240"
# 要查詢的地點經緯度
latitude = 23.5
longitude = 121
limit = 10  # 設置返回結果的限制數量

# 調用函數並獲取地理編碼數據
geocoding_info = get_geocoding_data(latitude, longitude, limit, api_key)

# 顯示地理編碼信息
display_geocoding_info(geocoding_info)
