# ZDI-24-782: PaperCut NG PrintDeployProxyController Incorrect Authorization Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-782
- **ZDI-CAN:** ZDI-CAN-22812
- **Date:** 2024-06-18
- **CVE:** CVE-2024-1222
- **CVSS:** 8.6
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:L/A:L
- **Affected Vendors:** PaperCut
- **Affected Products:** NG
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-782/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of PaperCut NG. Authentication is not required to exploit this vulnerability. The specific flaw exists within the PrintDeployProxyController class. The issue results from the incorrect authorization. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

PaperCut has issued an update to correct this vulnerability. More details can be found at: https://www.papercut.com/kb/Main/Security-Bulletin-March-2024

## Disclosure Timeline

- 2024-01-22 - Vulnerability reported to vendor
- 2024-06-18 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
