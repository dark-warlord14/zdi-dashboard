# ZDI-23-636: Schneider Electric APC Easy UPS Online updatePassword Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-636
- **ZDI-CAN:** ZDI-CAN-17583
- **Date:** 2023-05-17
- **CVE:** CVE-2022-42970
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** APC Easy UPS Online
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-636/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Schneider Electric APC Easy UPS Online. Authentication is not required to exploit this vulnerability. The specific flaw exists within the updatePassword function. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-22-347-02

## Disclosure Timeline

- 2022-06-17 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
