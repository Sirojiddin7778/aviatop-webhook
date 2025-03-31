from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "aviatop2025Token"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        if mode == 'subscribe' and token == VERIFY_TOKEN:
            print("✅ Webhook tasdiqlandi!")
            return challenge, 200
        else:
            return 'Verification failed', 403

    elif request.method == 'POST':
        print("✅ POST method chaqirildi")

        # Debug uchun har tomonlama tekshiruvlar
        print("🟨 Request headers:", dict(request.headers))
        print("🟧 Request body (raw):", request.get_data(as_text=True))

        try:
            data = request.json
            print("🟩 Parsed JSON:", data)
        except Exception as e:
            print("❌ JSON parsing xatosi:", str(e))
            return 'Bad Request', 400

        print("🗨️ Yangi Instagram xabar:", data)
        return 'OK', 200

# 🔁 Deauthorize va delete endpoint (majburiy emas, lekin kerak bo‘lishi mumkin)
@app.route('/deauthorize', methods=['POST'])
def deauthorize():
    print("❌ Instagram deauthorize request received.")
    return 'OK', 200

@app.route('/delete', methods=['POST'])
def delete():
    print("🗑️ Instagram delete request received.")
    return 'OK', 200

from waitress import serve

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
