# ZDI-25-755: (Pwn2Own) QNAP QHora-322 qsyslog-cli username Format String Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-755
- **ZDI-CAN:** ZDI-CAN-25672
- **Date:** 2025-07-31
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** QNAP
- **Affected Products:** QHora-322
- **Credit:** Chris Anastasio @mufinnnnnnn & Fabius Watson
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-755/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of QNAP QHora-322 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the username parameter provided to the qsyslog-cli executable. The issue results from the lack of proper validation of a user-supplied string before using it as a format specifier. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of root.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en-us/security-advisories

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-07-31 - Coordinated public release of advisory
- 2025-07-31 - Advisory Updated
