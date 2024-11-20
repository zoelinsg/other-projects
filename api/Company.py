import requests
import json

def fetch_data(api_url):
    """
    發送 HTTP GET 請求並取得 JSON 資料
    :param api_url: API 的 URL
    :return: 解析後的 JSON 資料，若失敗則回傳 None
    """
    try:
        # 發送 GET 請求
        response = requests.get(api_url)
        # 檢查回應狀態碼，若是 4xx 或 5xx 則拋出異常
        response.raise_for_status()
        # 將回應內容解析為 JSON 並回傳
        return response.json()
    except requests.exceptions.RequestException as e:
        # 捕捉任何請求相關的異常並輸出錯誤訊息
        print("Error fetching data:", e)
        return None

def display_data(data):
    """
    顯示指定的公司資訊
    :param data: 解析後的 JSON 資料
    """
    # 確認資料中有內容
    if data:
        # 取得第一筆公司的資訊（假設只有一筆資料）
        company_info = data[0]
        
        # 取出並顯示指定的欄位
        print(f"統一編號: {company_info.get('Business_Accounting_NO')}")
        print(f"公司名稱: {company_info.get('Company_Name')}")
        print(f"資本額: {company_info.get('Capital_Stock_Amount')}")
        print(f"負責人: {company_info.get('Responsible_Name')}")
        print(f"公司地址: {company_info.get('Company_Location')}")
        print(f"登記機關: {company_info.get('Register_Organization_Desc')}")
        print(f"公司設立日期: {company_info.get('Company_Setup_Date')}")
        print(f"核准變更日期: {company_info.get('Change_Of_Approval_Data')}")
    else:
        print("無法取得資料或資料為空")

def main():
    """
    主程式，設定統一編號並請求 API 取得公司資訊
    """
    # 統一編號
    Business_Accounting_NO = 85020415
    
    # API 的基本 URL，使用查詢參數過濾指定的統一編號
    api_url = (
        "http://data.gcis.nat.gov.tw/od/data/api/5F64D864-61CB-4D0D-8AD9-492047CC1EA6"
        "?$format=json"
        f"&$filter=Business_Accounting_NO eq {Business_Accounting_NO}"
        "&$skip=0&$top=50"
    )
    
    # 呼叫 fetch_data 函式取得資料
    data = fetch_data(api_url)
    
    # 顯示指定欄位的資料
    display_data(data)

if __name__ == "__main__":
    main()
