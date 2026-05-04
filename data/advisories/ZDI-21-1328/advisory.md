# ZDI-21-1328: Commvault CommCell CVSearchService Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1328
- **ZDI-CAN:** ZDI-CAN-13706
- **Date:** 2021-11-22
- **CVE:** CVE-2021-34993
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Commvault
- **Affected Products:** CommCell
- **Credit:** Brandon Perry, Justin Kennedy and Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1328/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Commvault CommCell. Authentication is not required to exploit this vulnerability. The specific flaw exists within the CVSearchService service. The issue results from the lack of proper validation prior to authentication. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Commvault has issued an update to correct this vulnerability. More details can be found at: https://documentation.commvault.com/securityadvisories/CV_2021_08_1.html

## Disclosure Timeline

- 2021-06-30 - Vulnerability reported to vendor
- 2021-11-22 - Coordinated public release of advisory
- 2025-08-04 - Advisory Updated
