
[comment]: # (Generated from JSON file by generate_feedback_md.py)
[comment]: # (Intended to be read in GitHub's markdown renderer. Apologies if the plaintext formatting is messy.)

# DawgInCastle's OWASP Falihax Hackathon Feedback
*Marked by [CyberSoc](https://cybersoc.org.uk/?r=falihax-marking-dawgincastle)*

This is DawgInCastle's specific feedback. See below for the full vunerability list, including ones you may have missed.

[General hackathon feedback with full vulnerability list and solutions](https://github.com/CyberSoc-Newcastle/owasp-falihax/blob/main/VULNS.md)
## Summary
**Total mark:** 20

A really good writeup of some security issues in this web app. Some big vulnerabilities were missed out, but those which were included are really interesting and show a good understanding, more from a black-box penetration testing point of view than the more traditional code review perspective.

No attempt was made to fix any of the vulnerabilities, however the writeup was great and still got many marks.

## Marking Scheme Used
We used the following marking scheme to award marks for each vulnerability, where the mark awarded for the vulnerability is the highest row in the following table fulfilled by your solution. A tick means you had to have done this to get the mark, a cross means this mark does not apply if you did this, and a dash means this is ignored for this possible mark. This mark scheme was decided after the entries had been submitted and was not known to entrants during the competition, although hints were provided as to what to include for good marks.

For each vulnerability, this is how many marks we would award:
| State a valid vulnerability | Show where it is in code | Demo it | Describe how it could be mitigated | Attempt a reasonable fix | Fix works | Explain your fix | Marks |
|-----------------------------|--------------------------|---------|------------------------------------|--------------------------|-----------|------------------|-------|
| ✔                           | ❌                        | ❌       | ❌                                  | ❌                        | -         | -                | 1     |
| ✔                           | ✔                        | ❌       | ❌                                  | ❌                        | -         | -                | 2     |
| ✔                           | -                        | ✔       | ❌                                  | ❌                        | -         | -                | 3     |
| ✔                           | -                        | -       | ✔                                  | ❌                        | -         | -                | 4     |
| ✔                           | -                        | -       | -                                  | ✔                        | ❌         | -                | 4     |
| -                           | -                        | ❌       | -                                  | ✔                        | ✔         | ❌                | 5     |
| -                           | -                        | ✔       | -                                  | ✔                        | ✔         | ❌                | 6     |
| -                           | -                        | -       | -                                  | ✔                        | ✔         | ✔                | 7     |

## Vulnerabilites Found
### [A01-03: No access control on the admin page](https://github.com/CyberSoc-Newcastle/owasp-falihax/blob/main/VULNS.md#a01-03-no-access-control-on-the-admin-page)
| State | Show | Demo | Mitigate | Attempt fix | Fix works | Explain fix | Mark |
|-------|------|------|----------|-------------|-----------|-------------|------|
| ✔     | ❌    | ✔    | ✔        | ❌           | ❌         | ❌           | 4    |


### [A02-01: Unsuitable use of ROT-13 "encryption"](https://github.com/CyberSoc-Newcastle/owasp-falihax/blob/main/VULNS.md#a02-01-unsuitable-use-of-rot-13-encryption)
| State | Show | Demo | Mitigate | Attempt fix | Fix works | Explain fix | Mark |
|-------|------|------|----------|-------------|-----------|-------------|------|
| ✔     | ❌    | ❌    | ❌        | ❌           | ❌         | ❌           | 1    |

Your reasoning about storing passwords on the database in plaintext is not entirely correct - the web app does use ROT-13 to encode passwords within the database. However, this is not really a secure form of encryption as it does not use any key so you are right there. Unfortunately since you only tried with numeric passwords (and ROT-13 does not modify numbers) you didn't spot this, nor did you notice it in the code. Therefore some marks were lost as the demonstration wasn't entirely accurate, you could also have reccommended some specific hashing algorithm for more marks.

Also, it would have been clearer and easier for you if you opened the database in an SQLite viewer tool such as the database explorer built into PyCharm. You appear to have opened the database in a text editor which isn't guaranteed to display database contents correctly.


### [A03-01: SQL Injection](https://github.com/CyberSoc-Newcastle/owasp-falihax/blob/main/VULNS.md#a03-01-sql-injection)
| State | Show | Demo | Mitigate | Attempt fix | Fix works | Explain fix | Mark |
|-------|------|------|----------|-------------|-----------|-------------|------|
| ✔     | ❌    | ✔    | ❌        | ❌           | ❌         | ❌           | 3    |

You are correct that the web app is vulnerable to SQL injection, however your claim that Flask sanitises input or protects against SQL injection attacks is not correct. This is especially the case here as we aren't using a Flask-related package to handle database tasks, we are using the standard `sqlite3` package with raw, unsanitised SQL statement strings.

We couldn't give you marks for mentioning securing against time attacks, because you didn't explain what specific kind of timing attack you meant or show how it could be used, or give examples of how it could be mitigated. But this was a good idea, it just needed expanding a little!


### [A04-02: No Password Strength Checks](https://github.com/CyberSoc-Newcastle/owasp-falihax/blob/main/VULNS.md#a04-02-no-password-strength-checks)
| State | Show | Demo | Mitigate | Attempt fix | Fix works | Explain fix | Mark |
|-------|------|------|----------|-------------|-----------|-------------|------|
| ✔     | ❌    | ✔    | ❌        | ❌           | ❌         | ❌           | 3    |

You could have also added how to mitigate this issue, perhaps by introducing password complexity requirements.


### [A04-03: No Rate Limiting](https://github.com/CyberSoc-Newcastle/owasp-falihax/blob/main/VULNS.md#a04-03-no-rate-limiting)
| State | Show | Demo | Mitigate | Attempt fix | Fix works | Explain fix | Mark |
|-------|------|------|----------|-------------|-----------|-------------|------|
| ✔     | ❌    | ❌    | ❌        | ❌           | ❌         | ❌           | 1    |

Good idea - although I think you missed it out of your main writeup! I only found reference to it in your conclusion rather than the main writeup, if there was more detail or examples on how to mitigate this then it would be worth more marks.


### [A04-04: Vulnerable to MITM attack](https://github.com/CyberSoc-Newcastle/owasp-falihax/blob/main/VULNS.md#a04-04-vulnerable-to-mitm-attack)
| State | Show | Demo | Mitigate | Attempt fix | Fix works | Explain fix | Mark |
|-------|------|------|----------|-------------|-----------|-------------|------|
| ✔     | ❌    | ✔    | ✔        | ❌           | ❌         | ❌           | 4    |

This is a good point that not many other people noticed! Your explanation is good, although take care to ensure the password is still hashed on the server for a second time to prevent replay attacks. See A04-04 in the general feedback for more information.

Also, some marks were missed here because you didn't really explain how XSS links into this issue - XSS could be a vulnerability in itself, albeit not one we found when searching, but it's not clear how it is connected to MITM attacks.


### [B01-01: Sort code generation denial of service vulnerability](https://github.com/CyberSoc-Newcastle/owasp-falihax/blob/main/VULNS.md#b01-01-sort-code-generation-denial-of-service-vulnerability)
| State | Show | Demo | Mitigate | Attempt fix | Fix works | Explain fix | Mark |
|-------|------|------|----------|-------------|-----------|-------------|------|
| ✔     | ❌    | ✔    | ✔        | ❌           | ❌         | ❌           | 4    |

Great work, you were the only entrant to notice this subtle vulnerability! Your reasoning was great and I really liked the step by step explanation with screenshots.

## Total mark
4 + 1 + 3 + 3 + 1 + 4 + 4 = 20

**Your total mark is 20**