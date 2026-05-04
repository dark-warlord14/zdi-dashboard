# ZDI-24-447: (0Day) D-Link D-View Use of Hard-coded Cryptographic Key Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-447
- **ZDI-CAN:** ZDI-CAN-21991
- **Date:** 2024-05-24
- **CVE:** CVE-2024-5296
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** D-View
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-447/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of D-Link D-View. Authentication is not required to exploit this vulnerability. The specific flaw exists within the TokenUtils class. The issue results from a hard-coded cryptographic key. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

08/22/23 – ZDI reported the vulnerability to the vendor 08/22/23 – The vendor acknowledged the receipt of the report 08/23/23 – The vendor communicated that the cases would be fixed in October, 2023 release 05/01/24 – ZDI notified the vendor of the intention to publish the case as 0-day advisory on 05/14/24 -- Mitigation: On May 14, 2024, the vendor informed ZDI about the software update v2.0.3.88 https://supportannouncement.us.dlink.com/security/publication.aspx?name=SAP10386

## Disclosure Timeline

- 2023-08-22 - Vulnerability reported to vendor
- 2024-05-24 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
