# ZDI-23-233: PaperCut NG SetupCompleted Improper Access Control Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-233
- **ZDI-CAN:** ZDI-CAN-18987
- **Date:** 2023-03-14
- **CVE:** CVE-2023-27350
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** PaperCut
- **Affected Products:** NG
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-233/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of PaperCut NG. Authentication is not required to exploit this vulnerability. The specific flaw exists within the SetupCompleted class. The issue results from improper access control. An attacker can leverage this vulnerability to bypass authentication and execute arbitrary code in the context of SYSTEM.

## Additional Details

PaperCut has issued an update to correct this vulnerability. More details can be found at: https://www.papercut.com/kb/Main/PO-1216-and-PO-1219

## Disclosure Timeline

- 2023-01-10 - Vulnerability reported to vendor
- 2023-03-14 - Coordinated public release of advisory
- 2023-04-19 - Advisory Updated
