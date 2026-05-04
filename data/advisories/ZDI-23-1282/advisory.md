# ZDI-23-1282: Microsoft Teams Pluginhost Prototype Pollution Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1282
- **ZDI-CAN:** ZDI-CAN-21201
- **Date:** 2023-08-30
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Teams
- **Credit:** Li Jiantao (@CurseRed), Ngo Wei Lin (@Creastery), Pan Zhenpeng (@Peterpan980927), Poh Jia Hao (@Chocologicall) of STAR Labs SG Pte. Ltd.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1282/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Microsoft Teams. An attacker must first obtain the ability to execute script within the application window in order to exploit this vulnerability. The specific flaw exists within the Pluginhost window. The issue results from the lack of control over modifications to attributes of object prototypes. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-us/security-guidance/researcher-acknowledgments-online-services

## Disclosure Timeline

- 2023-05-19 - Vulnerability reported to vendor
- 2023-08-30 - Coordinated public release of advisory
