# ZDI-24-779: PaperCut NG VendorKeys Hardcoded Credentials Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-779
- **ZDI-CAN:** ZDI-CAN-22165
- **Date:** 2024-06-18
- **CVE:** CVE-2024-1223
- **CVSS:** 8.2
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:L/A:N
- **Affected Vendors:** PaperCut
- **Affected Products:** NG
- **Credit:** Ahmed Y. Elmogy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-779/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of PaperCut NG. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of a VendorKeys object. The issue results from the use of hard-coded credentials. An attacker can leverage this vulnerability to bypass authentication on the External Devices API.

## Additional Details

PaperCut has issued an update to correct this vulnerability. More details can be found at: https://www.papercut.com/kb/Main/Security-Bulletin-March-2024

## Disclosure Timeline

- 2024-01-17 - Vulnerability reported to vendor
- 2024-06-18 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
