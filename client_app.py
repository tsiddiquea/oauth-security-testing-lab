import requests
from config import CLIENT_ID

provider = "http://localhost:8080"

redirect_uri = input("Enter redirect URI: ")

auth_url = f"{provider}/auth?client_id={CLIENT_ID}&redirect_uri={redirect_uri}"

print("\nLogin URL:")
print(auth_url)

response = requests.get(auth_url, allow_redirects=False)

redirect_location = response.headers.get("Location")

print("\nRedirected to:")
print(redirect_location)


if redirect_location is None:
    print("\nOAuth provider rejected the request (secure validation).")
    exit()

code = redirect_location.split("code=")[1].split("&")[0]

token_resp = requests.get(f"{provider}/token?code={code}")
token = token_resp.json()["access_token"]

print("\nAccess token received:", token)

user = requests.get(f"{provider}/userinfo?token={token}")

if user.status_code == 200:
    print("\nUser data accessed successfully")
else:
    print("\nFailed to access user data")