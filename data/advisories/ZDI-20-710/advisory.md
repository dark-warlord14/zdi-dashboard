# ZDI-20-710: IBM Spectrum Protect Plus Hardcoded Username And Password Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-710
- **ZDI-CAN:** ZDI-CAN-9751
- **Date:** 2020-06-15
- **CVE:** CVE-2020-4216
- **CVSS:** 7.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** IBM
- **Affected Products:** Spectrum Protect Plus
- **Credit:** Jeremy Brown
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-710/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on vulnerable installations of IBM Spectrum Protect Plus. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of login requests to the Discovery Server service. The product contains a hard-coded password for an account. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: https://www.ibm.com/support/pages/node/6221332

## Disclosure Timeline

- 2019-12-11 - Vulnerability reported to vendor
- 2020-06-15 - Coordinated public release of advisory
