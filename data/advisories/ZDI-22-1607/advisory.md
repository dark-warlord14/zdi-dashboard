# ZDI-22-1607: (Pwn2Own) Microsoft Teams Unnecessary Privileges Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1607
- **ZDI-CAN:** ZDI-CAN-17526
- **Date:** 2022-11-21
- **CVE:** N/A
- **CVSS:** 4.8
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Teams
- **Credit:** Masato Kinugawa
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1607/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Microsoft Teams. An attacker must first obtain the ability to execute script within the application window in order to exploit this vulnerability. The specific flaw exists within the parameters passed to the Teams.exe process on startup. As a result, the application executes with unnecessary privileges. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Fixed on August 31, 2022 https://msrc.microsoft.com/update-guide/acknowledgement/online

## Disclosure Timeline

- 2022-06-10 - Vulnerability reported to vendor
- 2022-11-21 - Coordinated public release of advisory
