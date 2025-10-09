# Educational Demo: Insecure Login Page (HTTP)

## Disclaimer

This project is a **minimal educational demonstration** of how login pages that use **HTTP instead of HTTPS** can be exploited in unsafe environments. It does **not target any real-world system, website, or organization**.

It was created and tested **entirely in a local, offline lab environment**, using:

- A basic `index.html` page mimicking a **generic** login form  
- A simple Python Flask server (`server.py`) that receives and logs submitted credentials

---

## Warning

This repository is intended **only for educational and awareness purposes**. It is a **sanitized and redacted demo**, built to demonstrate how the lack of HTTPS can expose login credentials to interception and spoofing attacks like MITM.

### What This Is NOT:
- An exploit or hacking tool  
- A phishing page targeting any real site  
- A replica of any university or organization login page  
- Meant for use outside of isolated environments  

---

## What This Is:
- A safe example to highlight insecure credential transmission  
- An illustration of the dangers of using HTTP for login forms  
- A resource for cybersecurity learners and ethical hackers  

---

## Responsible Disclosure

This repository was created **after identifying a login page served over HTTP** on a public domain. The issue was reported to the relevant organization through **responsible disclosure**. No exploitation, unauthorized access, or interaction with real systems occurred at any point.

---

## Usage Restrictions

You must **not** use this code on real-world websites, networks, or domains.  
Any unauthorized use of this project for malicious purposes is strictly forbidden and may be illegal.

---

## Files

- `server.py` – Simple Flask server to receive POSTed credentials  
- `templates/index.html` – Generic login page for demonstration  

---

## Educational Context

This demo aligns with the following ethical hacking and security learning goals:

- Understanding the need for HTTPS (SSL/TLS)
- Demonstrating basic credential interception scenarios
- Encouraging responsible vulnerability disclosure
- Building awareness of insecure web practices

---

**Use responsibly. Always test in isolated environments. Get permission first.**  
*Ethical hacking begins with ethics.*

