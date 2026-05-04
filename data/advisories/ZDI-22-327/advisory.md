# ZDI-22-327: (Pwn2Own) Lexmark MC3224i pagemaker Insufficient Session Expiration Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-327
- **ZDI-CAN:** ZDI-CAN-15925
- **Date:** 2022-02-15
- **CVE:** CVE-2021-44738
- **CVSS:** 7.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N
- **Affected Vendors:** Lexmark
- **Affected Products:** MC3224i
- **Credit:** Christopher Anastasio @mufinnnnnnn
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-327/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Lexmark MC3224i printers. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the remote object server. The issue results from the lack of an appropriate expiration mechanism for session IDs. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute arbitrary code in the context of the web admin user.

## Additional Details

Lexmark has issued an update to correct this vulnerability. More details can be found at: https://publications.lexmark.com/publications/security-alerts/CVE-2021-44738.pdf

## Disclosure Timeline

- 2021-12-30 - Vulnerability reported to vendor
- 2022-02-15 - Coordinated public release of advisory
