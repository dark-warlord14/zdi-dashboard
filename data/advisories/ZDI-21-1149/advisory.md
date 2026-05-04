# ZDI-21-1149: Schneider Electric IGSS Missing Authentication Arbitrary File Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1149
- **ZDI-CAN:** ZDI-CAN-13893
- **Date:** 2021-10-14
- **CVE:** CVE-2021-22805
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N
- **Affected Vendors:** Schneider Electric
- **Affected Products:** IGSS
- **Credit:** Vyacheslav Moskvin
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1149/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files on affected installations of Schneider Electric IGSS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of commands sent to the server. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to delete files in the context of the current user.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-285-03

## Disclosure Timeline

- 2021-07-15 - Vulnerability reported to vendor
- 2021-10-14 - Coordinated public release of advisory
