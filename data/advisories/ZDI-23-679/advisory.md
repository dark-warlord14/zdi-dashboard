# ZDI-23-679: Delta Electronics InfraSuite Device Master CheckgRPCAuthentication Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-679
- **ZDI-CAN:** ZDI-CAN-19281
- **Date:** 2023-05-17
- **CVE:** CVE-2023-1136
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** InfraSuite Device Master
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-679/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Delta Electronics InfraSuite Device Master. Authentication is not required to exploit this vulnerability. The specific flaw exists within the CheckgRPCAuthentication function. When parsing serialized objects, the server does not properly validate user-supplied data. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-23-080-02

## Disclosure Timeline

- 2022-10-31 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
