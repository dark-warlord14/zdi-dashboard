# ZDI-23-714: D-Link D-View Use of Hard-coded Cryptographic Key Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-714
- **ZDI-CAN:** ZDI-CAN-19659
- **Date:** 2023-05-24
- **CVE:** CVE-2023-32169
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** D-View
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-714/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of D-Link D-View. Authentication is not required to exploit this vulnerability. The specific flaw exists within the TokenUtils class. The issue results from a hard-coded cryptographic key. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10332

## Disclosure Timeline

- 2022-12-23 - Vulnerability reported to vendor
- 2023-05-24 - Coordinated public release of advisory
