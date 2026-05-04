# ZDI-24-786: PaperCut NG print.script.sandboxed Exposed Dangerous Function Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-786
- **ZDI-CAN:** ZDI-CAN-20965
- **Date:** 2024-06-18
- **CVE:** CVE-2023-39470
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** PaperCut
- **Affected Products:** NG
- **Credit:** Trinity Cyber
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-786/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of PaperCut NG. Authentication is required to exploit this vulnerability. The specific flaw exists within the management of the print.script.sandboxed setting. The issue results from the exposure of a dangerous function. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

PaperCut has issued an update to correct this vulnerability. More details can be found at: https://www.papercut.com/kb/Main/SecurityBulletinJune2023/

## Disclosure Timeline

- 2023-04-20 - Vulnerability reported to vendor
- 2024-06-18 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
