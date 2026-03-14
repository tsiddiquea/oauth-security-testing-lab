from flask import Flask, request, redirect, jsonify
import secrets
from config import ALLOWED_REDIRECT
from logger import log_event

app = Flask(__name__)

auth_codes = {}
tokens = {}

@app.route("/auth")
def auth():
    client_id = request.args.get("client_id")
    redirect_uri = request.args.get("redirect_uri")
    state = request.args.get("state")

    if redirect_uri != ALLOWED_REDIRECT:
        log_event("Blocked open redirect attempt")
        return jsonify({"error": "invalid redirect_uri"}), 400

    if not state:
        log_event("Missing state parameter")
        return jsonify({"error": "missing state"}), 400

    code = secrets.token_hex(8)
    auth_codes[code] = client_id

    return redirect(f"{redirect_uri}?code={code}&state={state}")

@app.route("/token", methods=["POST"])
def token():
    code = request.form.get("code")

    if code not in auth_codes:
        return jsonify({"error": "invalid code"}), 400

    token = secrets.token_hex(16)
    tokens[token] = "demo_user"

    return jsonify({"access_token": token})

@app.route("/userinfo")
def userinfo():
    token = request.headers.get("Authorization")

    if token not in tokens:
        return jsonify({"error": "invalid token"}), 401

    return jsonify({"user": tokens[token]})

if __name__ == "__main__":
    print("Secure OAuth provider running on http://localhost:8080")
    app.run(port=8080)