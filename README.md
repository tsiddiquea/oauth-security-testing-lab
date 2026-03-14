# OAuth Misconfiguration Attack Simulation Lab

## Overview

The OAuth Misconfiguration Lab is a cybersecurity research project that demonstrates how improper validation of OAuth authorization flows can lead to serious security vulnerabilities such as open redirect exploitation and authorization code leakage.

This project simulates both:

* A secure OAuth provider implementation
* A vulnerable OAuth provider implementation
* An attacker simulation environment
* A client application requesting authorization
* A security logging mechanism

The lab allows practical experimentation with OAuth security weaknesses and defensive validation techniques, providing a realistic hands-on environment for understanding modern authentication risks.


## Objectives

This project was designed to:

* Demonstrate real-world OAuth attack surfaces
* Simulate authorization code interception attacks
* Show the importance of redirect URI validation
* Compare secure vs insecure OAuth implementations
* Provide defensive engineering insights
* Build practical understanding of authentication security



## System Architecture

The lab consists of multiple interacting components:

### 1. Secure OAuth Provider

Implements:

* Redirect URI allow-listing
* State parameter validation
* Authorization code generation
* Token exchange through POST requests
* Access control enforcement
* Security event logging

### 2. Vulnerable OAuth Provider

Intentionally misconfigured to demonstrate:

* Missing redirect validation
* Token leakage through GET requests
* Open redirect exploitation
* Weak authorization flow handling

### 3. Client Application

Simulates a legitimate OAuth client that:

* Requests authorization codes
* Exchanges codes for access tokens
* Accesses protected user resources

### 4. Attacker Simulation Module

Demonstrates:

* Malicious redirect URI injection
* Authorization code interception
* Token acquisition through insecure flow

### 5. Security Logger

Tracks:

* Open redirect attempts
* Invalid authorization requests
* Suspicious authentication behavior



## Key Security Concepts Demonstrated

This lab implements and illustrates:

* OAuth 2.0 Authorization Code Flow
* Redirect URI validation importance
* State parameter protection against CSRF
* Token handling security
* Access token exposure risks
* Authentication flow integrity


## Example Attack Scenario

The attacker crafts a malicious authorization request:
```
http://localhost:8080/auth?client_id=app&redirect_uri=http://evil.com
```

If the OAuth provider is vulnerable:

* Authorization code is redirected to attacker domain
* Attacker can exchange the code for an access token
* Protected user data can be accessed

If the provider is secure:

* Request is rejected
* Security log entry is created
* Attack is prevented


## Example Terminal Workflow

### Step 1 — Start OAuth Provider
```
python oauth_provider_secure.py
```
Output:
```
Secure OAuth provider running on http://localhost:8080
```
## Step 2 — Run Client
```
python client_app.py
```

Output:
```
Login URL:
http://localhost:8080/auth?client_id=app&redirect_uri=http://localhost:9000/callback
Access token received: 4f8a21c9b3...
User data accessed successfully
```
### Step 3 — Run Attacker Simulation
```
python attacker_simulator.py
```

Output (vulnerable provider):
```
Simulating OAuth Misconfiguration Attack
Redirected to: http://evil.com?code=ab91e8...
Authorization code leaked to attacker
```

Output (secure provider):
```
OAuth provider rejected malicious redirect
Security event logged
```


## Project Structure
```
oauth-misconfiguration-lab/
│
├── oauth_provider_secure.py
├── oauth_provider_vulnerable.py
├── client_app.py
├── attacker_simulator.py
├── config.py
├── logger.py
├── oauth_security_log.txt
└── README.md
```


## Technologies Used

* Python
* Flask Web Framework
* Requests Library
* REST API Simulation
* Secure Token Generation
* Authentication Flow Modeling


## Performance Characteristics

* Lightweight simulation suitable for local execution
* Minimal system resource consumption
* Fast authorization code generation
* Real-time logging for security monitoring


## Security & Ethical Use

This project is intended strictly for:

* Cybersecurity education
* Secure authentication research
* Defensive engineering practice
* Academic experimentation

It must only be used in controlled and authorized environments.


## Learning Outcomes

By completing this project, the following competencies are demonstrated:

* Practical understanding of OAuth vulnerabilities
* Secure authentication architecture design
* Attack simulation and threat modeling
* Defensive validation implementation
* Security logging and monitoring strategies
* Application-layer security engineering


## Author

Developed as part of an independent cybersecurity learning initiative focused on authentication security, vulnerability research, and secure system design.


## License

This project is released for educational and research purposes.
Use responsibly.
