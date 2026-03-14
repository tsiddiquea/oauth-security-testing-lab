# OAuth Security Tesing Lab

## Project Overview

The OAuth Security Testing Lab is a hands-on cybersecurity project designed to demonstrate how improper implementation of the OAuth authorization framework can introduce critical security vulnerabilities in modern web systems.

This lab simulates both secure and vulnerable OAuth provider behaviors, allowing practical exploration of real-world authentication flaws such as:

* Open redirect exploitation
* Authorization code leakage
* Improper token transmission
* Weak validation of redirect URIs
* Missing request state verification

The project provides a controlled environment for analyzing authentication weaknesses and understanding how secure design principles prevent identity-based attacks.


## Objectives of the Lab

This project was developed to achieve the following security learning goals:

* Understand OAuth authorization workflow at a practical level
* Demonstrate how misconfigurations lead to account compromise risks
* Explore attacker techniques used to intercept authorization data
* Implement logging mechanisms to detect suspicious authentication events
* Compare vulnerable and hardened authentication server behavior

The lab bridges theoretical security knowledge with real implementation logic.



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



## Security Concepts Demonstrated

This lab covers several important application security principles:

* Authorization code interception attacks
* Authentication flow manipulation
* Open redirect exploitation risks
* Token confidentiality protection
* Defensive validation logic implementation
* Security monitoring and incident logging

The project reflects realistic identity security threats faced by modern SaaS platforms and web applications.


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
oauth-security-testing-lab/
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

* Lightweight Flask-based simulation environment
* Minimal resource usage suitable for local testing
* Fast authorization flow simulation
* Real-time logging of authentication events

The system is optimized for educational experimentation rather than production deployment.

## Ethical Use Statement

This project is intended solely for:

* Cybersecurity education
* Secure software engineering practice
* Authentication protocol research
* Defensive security training

It must only be executed in controlled lab environments and never against real systems without authorization.

## Learning Outcomes

Through this project, the following competencies are demonstrated:

* Practical understanding of identity and access management risks
* Secure authentication system design principles
* Attack modeling against authorization protocols
* Defensive coding and validation strategies
* Security logging and monitoring concepts
* Application security research methodology



## Author

Developed as part of an independent cybersecurity learning initiative focused on real-world vulnerability analysis and secure authentication engineering.

## License

This project is provided for educational and research purposes.
Use responsibly and only within authorized environments.
