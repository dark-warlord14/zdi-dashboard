# ZDI-23-1767: Microsoft Teams Isolated Webview Prototype Pollution Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1767
- **ZDI-CAN:** ZDI-CAN-20812
- **Date:** 2023-12-13
- **CVE:** N/A
- **CVSS:** 7.1
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:H/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Teams
- **Credit:** Li Jiantao (@CurseRed), Ngo Wei Lin (@Creastery), Pan Zhenpeng (@Peterpan980927), Poh Jia Hao (@Chocologicall) of STAR Labs SG Pte. Ltd.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1767/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Microsoft Teams. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Isolated Webview component. The issue results from the lack of control over modifications to attributes of object prototypes. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-us/security-guidance/researcher-acknowledgments-online-services

## Disclosure Timeline

- 2023-05-19 - Vulnerability reported to vendor
- 2023-12-13 - Coordinated public release of advisory
