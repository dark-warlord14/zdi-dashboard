# ZDI-25-1060: Senstar Symphony FetchStoredLicense Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1060
- **ZDI-CAN:** ZDI-CAN-26908
- **Date:** 2025-12-10
- **CVE:** CVE-2025-12491
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Senstar
- **Affected Products:** Symphony
- **Credit:** Gert Keldermans & Nabeel Ahmed of NTT Belgium
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1060/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Senstar Symphony. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of FetchStoredLicense method. The issue results from the exposure of sensitive information. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Fixed in version 8.11 and all previous versions

## Disclosure Timeline

- 2025-07-08 - Vulnerability reported to vendor
- 2025-12-10 - Coordinated public release of advisory
- 2025-12-10 - Advisory Updated
