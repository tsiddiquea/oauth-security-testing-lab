from flask import Flask, request, redirect, jsonify
import secrets

app = Flask(__name__)

auth_codes = {}
tokens = {}

@app.route("/auth")
def auth():
    client_id = request.args.get("client_id")
    redirect_uri = request.args.get("redirect_uri")

    code = secrets.token_hex(8)
    auth_codes[code] = client_id

    # VULNERABILITY: redirect URI not validated
    return redirect(f"{redirect_uri}?code={code}")

@app.route("/token")
def token():
    code = request.args.get("code")

    if code not in auth_codes:
        return jsonify({"error": "invalid code"}), 400

    token = secrets.token_hex(16)
    tokens[token] = "demo_user"

    # VULNERABILITY: token returned via GET (URL)
    return jsonify({"access_token": token})

@app.route("/userinfo")
def userinfo():
    token = request.args.get("token")

    if token not in tokens:
        return jsonify({"error": "invalid token"}), 401

    return jsonify({"user": tokens[token]})

if __name__ == "__main__":
    print("OAuth provider running on http://localhost:8080")
    app.run(port=8080)