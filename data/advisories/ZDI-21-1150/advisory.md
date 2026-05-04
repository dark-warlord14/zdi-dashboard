# ZDI-21-1150: Schneider Electric IGSS dc.exe Missing Authentication Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1150
- **ZDI-CAN:** ZDI-CAN-14460
- **Date:** 2021-10-14
- **CVE:** CVE-2021-22804
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Schneider Electric
- **Affected Products:** IGSS
- **Credit:** Vyacheslav Moskvin
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1150/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Schneider Electric IGSS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of TCP traffic by the dc.exe process. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to disclose information in the context of the current user.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-285-03

## Disclosure Timeline

- 2021-07-20 - Vulnerability reported to vendor
- 2021-10-14 - Coordinated public release of advisory
