# 使用 Python 連接到 API
import requests  # 導入 requests 庫來發送 HTTP 請求

# API 的基本 URL
base_url = "https://pokeapi.co/api/v2/"

# 定義一個函數來根據寶可夢名稱獲取信息
def get_pokemon_info(name):
    # 格式化 URL，將 base_url 和寶可夢名稱結合
    url = f"{base_url}pokemon/{name}"  
    response = requests.get(url)  # 發送 GET 請求
    # 檢查 HTTP 回應狀態碼是否為 200 (表示成功)
    if response.status_code == 200:
        pokemon_data = response.json()  # 解析回應的 JSON 數據
        return pokemon_data  # 返回寶可夢數據
    else:
        # 如果回應不是 200，則打印錯誤訊息
        print(f"無法獲取數據，狀態碼: {response.status_code}")

# 設定寶可夢的名稱
pokemon_name = "typhlosion"

# 調用函數獲取寶可夢信息
pokemon_info = get_pokemon_info(pokemon_name)

# 如果成功獲取寶可夢信息，則打印詳細信息
if pokemon_info:
    print(f"名稱: {pokemon_info['name'].capitalize()}")  # 輸出寶可夢名稱（首字母大寫）
    print(f"ID: {pokemon_info['id']}")  # 輸出寶可夢的 ID
    print(f"身高: {pokemon_info['height']}")  # 輸出寶可夢的身高
    print(f"體重: {pokemon_info['weight']}")  # 輸出寶可夢的體重
   