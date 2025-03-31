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
        data = request.json
        print("💬 Yangi Instagram xabar:", data)
        return 'OK', 200

# 👇 BULARNI YANGI QO‘SHDIK:
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
