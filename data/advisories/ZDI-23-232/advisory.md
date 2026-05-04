# ZDI-23-232: PaperCut NG SecurityRequestFilter Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-232
- **ZDI-CAN:** ZDI-CAN-19226
- **Date:** 2023-03-14
- **CVE:** CVE-2023-27351
- **CVSS:** 8.2
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:L/A:N
- **Affected Vendors:** PaperCut
- **Affected Products:** NG
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-232/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of PaperCut NG. Authentication is not required to exploit this vulnerability. The specific flaw exists within the SecurityRequestFilter class. The issue results from improper implementation of the authentication algorithm. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

PaperCut has issued an update to correct this vulnerability. More details can be found at: https://www.papercut.com/kb/Main/PO-1216-and-PO-1219

## Disclosure Timeline

- 2023-01-10 - Vulnerability reported to vendor
- 2023-03-14 - Coordinated public release of advisory
- 2023-04-19 - Advisory Updated
