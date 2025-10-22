from flask import Flask, request, jsonify
import json

# Khởi tạo ứng dụng Flask
# Vercel sẽ tự động tìm biến tên 'app' này
app = Flask(__name__)
@app.route("/", methods=['GET'])
def home():
    return "welcome!"
@app.route("/sepay-webhook", methods=['POST'])
def sepay_webhook():
    if not request.is_json:
        return jsonify({"error": "Invalid data format, JSON expected"}), 400

    data = request.get_json()
    
    print("="*30)
    print("ĐÃ NHẬN DỮ LIỆU TỪ SEPAY WEBHOOK:")
    print(json.dumps(data, indent=2, ensure_ascii=False)) 
    print("="*30)

    # ... (Logic xử lý của bạn ở đây) ...

    return jsonify({"status": "success", "message": "Webhook received"}), 200

# KHÔNG CẦN PHẦN `if __name__ == '__main__':` NỮA