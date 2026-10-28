# Secure Coding Review using Python

## Project Overview

This project is a Secure Coding Review developed using Python as part of the CodeAlpha Cyber Security Internship. The project focuses on identifying common security vulnerabilities in a Python-based user login system and improving the code using secure coding practices.

The application demonstrates security issues such as SQL injection and plaintext password storage in a vulnerable login system, then implements security improvements using parameterized SQL queries, bcrypt password hashing, and input validation.

The project uses static analysis tools and manual code inspection to identify vulnerabilities and document the security improvements.

---

## Features

* Review vulnerable Python source code
* Identify potential SQL injection vulnerabilities
* Identify insecure plaintext password storage
* Implement parameterized SQL queries
* Use bcrypt for password hashing
* Validate user input
* Perform static code analysis
* Compare vulnerable and secure code
* Document security findings and remediation
* Test valid and invalid login attempts

---

## Technologies Used

* Python 3.11
* SQLite
* bcrypt
* Bandit
* Pylint
* Visual Studio Code
* Windows Command Prompt

---

## Installation

Install the required Python libraries:

```bash
pip install bandit pylint bcrypt
```

---

## How to Run

### Run the Vulnerable Login System

```bash
python vulnerable\login.py
```

### Run the Secure Login System

```bash
python secure\login.py
```

Use the demo credentials configured in the secure application to test a successful login.

**Note:** The demo password is intended only for local testing and must not be used in a production application.

---

## Security Analysis

### Bandit

Run Bandit on the vulnerable code:

```bash
bandit -r vulnerable -f txt -o reports\vulnerable_bandit_report.txt
```

Run Bandit on the secure code:

```bash
bandit -r secure -f txt -o reports\secure_bandit_report.txt
```

### Pylint

Run Pylint on the vulnerable code:

```bash
pylint vulnerable\login.py
```

Run Pylint on the secure code:

```bash
pylint secure\login.py
```

---

## Security Improvements

* Replaced dynamically constructed SQL queries with parameterized queries.
* Replaced plaintext password storage with bcrypt password hashing.
* Added input validation for usernames and passwords.
* Used a generic error message for unsuccessful login attempts.
* Improved code quality and readability.

---

## Testing Results

| Test | Result |
|---|---|
| Valid login | Passed |
| Invalid login | Passed |
| Bandit scan on secure code | No issues identified |
| Pylint on secure code | 10.00/10 |

Static analysis did not identify potential issues in the secure version. These results do not guarantee that the application is free from all vulnerabilities.

---

## Project Structure

```text
CodeAlpha_SecureCodingReview
│
├── vulnerable
│   └── login.py
│
├── secure
│   └── login.py
│
├── reports
│   ├── security_audit.md
│   ├── vulnerable_bandit_report.txt
│   ├── secure_bandit_report.txt
│   └── secure_pylint_report.txt
│
├── requirements.txt
└── README.md
```

---

## Learning Outcomes

* Understanding common software security vulnerabilities
* Identifying SQL injection risks
* Understanding secure password storage
* Applying secure coding practices in Python
* Using Bandit for static security analysis
* Using Pylint for code quality analysis
* Performing manual code review
* Documenting vulnerabilities and remediation

---

## Author

Charan M R

CodeAlpha Cyber Security Internship Project

Task 3: Secure Coding Review
