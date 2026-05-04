# ZDI-23-450: (Pwn2Own) Triangle MicroWorks SCADA Data Gateway Restore Workspace Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-450
- **ZDI-CAN:** ZDI-CAN-17227
- **Date:** 2023-04-14
- **CVE:** CVE-2022-0369
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Triangle MicroWorks
- **Affected Products:** SCADA Data Gateway
- **Credit:** Steven Seeley (mr_me) and Chris Anastasio (muffin) of Incite Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-450/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Triangle MicroWorks SCADA Data Gateway. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the Restore Workspace feature. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Fixed in Version 5.01.02

## Disclosure Timeline

- 2022-05-09 - Vulnerability reported to vendor
- 2023-04-14 - Coordinated public release of advisory
