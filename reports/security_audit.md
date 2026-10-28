\# Security Audit Report



\## Project Overview



This security audit was conducted as part of the CodeAlpha Cyber Security Internship, Task 3: Secure Coding Review.



The project reviews a Python-based user login system to identify security vulnerabilities and implement secure coding practices. The vulnerable and secure versions were analyzed using Bandit, Pylint and manual code inspection.



\---



\## Objectives



\* Identify security vulnerabilities in Python source code.

\* Detect potential SQL injection vulnerabilities.

\* Identify insecure password storage.

\* Apply secure coding practices.

\* Perform static code analysis.

\* Compare vulnerable and secure implementations.

\* Document findings and remediation.



\---



\## Tools Used



\* Python 3.11.9

\* Bandit 1.9.4

\* Pylint 4.1.1

\* SQLite

\* bcrypt

\* Visual Studio Code



\---



\## Security Findings



\### 1. SQL Injection



\*\*Severity:\*\* Medium  

\*\*Confidence:\*\* Low  

\*\*CWE:\*\* CWE-89  

\*\*Detection:\*\* Bandit and manual code review



\*\*Description:\*\*



The vulnerable version constructs an SQL query dynamically using user input. This can allow malicious input to alter the intended SQL query.



\*\*Remediation:\*\*



Parameterized SQL queries were implemented in the secure version to separate SQL commands from user-supplied values.



\### 2. Plaintext Password Storage



\*\*Severity:\*\* High  

\*\*Detection:\*\* Manual code review



\*\*Description:\*\*



The vulnerable version stores passwords in plaintext, which can expose user credentials if the database is accessed by an unauthorized person.



\*\*Remediation:\*\*



The secure version uses bcrypt to hash passwords before storing them in the database. During login, bcrypt is used to verify the entered password against the stored hash.



\---



\## Static Analysis Results



\### Bandit Results



| Analysis | Vulnerable Version | Secure Version |

|---|---:|---:|

| High severity | 0 | 0 |

| Medium severity | 1 | 0 |

| Low severity | 0 | 0 |

| Total issues | 1 | 0 |



The vulnerable version reported a possible SQL injection issue, identified as `B608`, with medium severity and low confidence.



The secure version reported no issues identified by Bandit.



\### Pylint Results



| Version | Score |

|---|---:|

| Vulnerable Version | 8.08/10 |

| Secure Version | 10.00/10 |



The secure version achieved a Pylint score of 10.00/10, reflecting improved code quality according to Pylint's checks.



\---



\## Functional Testing



| Test Case | Expected Result | Actual Result | Status |

|---|---|---|---|

| Valid username and password | Login successful | Login successful | Pass |

| Invalid username and password | Invalid username or password | Invalid username or password | Pass |



Both functional tests produced the expected results.



\---



\## Security Improvements



\* Implemented parameterized SQL queries to reduce SQL injection risk.

\* Replaced plaintext password storage with bcrypt password hashing.

\* Added username and password input validation.

\* Used a generic error message for failed login attempts.

\* Improved code quality and readability.



\---



\## Conclusion



The security review identified a potential SQL injection vulnerability and plaintext password storage in the vulnerable login system. These issues were addressed in the secure version using parameterized SQL queries and bcrypt password hashing.



The secure version received no issues identified by Bandit and achieved a Pylint score of 10.00/10. Both valid and invalid login tests passed.



These results demonstrate the implemented security improvements but do not guarantee that the application is completely free from vulnerabilities. Additional testing would be required before using the system in production.



\---



\## Author



Charan M R



CodeAlpha Cyber Security Internship Project



Task 3: Secure Coding Review



