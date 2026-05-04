# ZDI-20-809: C-MORE HMI EA9 EA-HTTP Improper Input Validation Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-809
- **ZDI-CAN:** ZDI-CAN-10527
- **Date:** 2020-07-07
- **CVE:** CVE-2020-10922
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** C-MORE
- **Affected Products:** HMI EA9
- **Credit:** evanslify
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-809/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of C-More HMI EA9 touch screen panels. Authentication is not required to exploit this vulnerability. The specific flaw exists within the EA-HTTP.exe process. The issue results from the lack of proper input validation prior to further processing user requests. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Fixed in version 6.60

## Disclosure Timeline

- 2020-06-25 - Vulnerability reported to vendor
- 2020-07-07 - Coordinated public release of advisory
- 2020-07-08 - Advisory Updated
