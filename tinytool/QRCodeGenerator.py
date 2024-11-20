# QR Code Generator
# 引入 qrcode 模組，用於生成 QR code
import qrcode

# 定義一個函式來生成 QR code，參數為需要轉成 QR code 的文字內容
def generate_qrcode(text):
    # 建立 QRCode 物件，設置版本、容錯率、每個 box 的大小以及邊框大小
    qr = qrcode.QRCode(
        version=1,  # 設置 QR code 的版本（尺寸大小）
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # 設置錯誤容錯率，L 表示 7% 的錯誤可被修正
        box_size=10,  # 設置每個 box 的像素大小
        border=4,  # 設置邊框的大小（box 的數量）
    )

    # 向 QRCode 物件中添加數據（即需要轉為 QR code 的內容）
    qr.add_data(text)
    qr.make(fit=True)  # 自動調整 QR code 大小以適應內容

    # 生成圖片，設置填充顏色為黑色，背景顏色為白色
    img = qr.make_image(fill_color="black", back_color="white")

    # 將生成的 QR code 圖片保存到指定的路徑
    img.save("img/qr-img001.png")

# 從使用者輸入獲取 URL 或其他文字內容，並生成對應的 QR code
url = input("Enter your url: ")  # 提示使用者輸入 URL
generate_qrcode(url)  # 調用函式生成 QR code
