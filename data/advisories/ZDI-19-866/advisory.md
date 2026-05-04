# ZDI-19-866: NETGEAR AC1200 mini_httpd Poison Null Byte Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-866
- **ZDI-CAN:** ZDI-CAN-8616
- **Date:** 2019-10-10
- **CVE:** CVE-2019-17137
- **CVSS:** 9.4
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:L/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** AC1200
- **Credit:** Michael Flanders of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-866/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of NETGEAR AC1200 Smart WiFi Router. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of path strings. By inserting a null byte into the path, the user can skip most authentication checks. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Fixed in version 1.2.0.62

## Disclosure Timeline

- 2019-04-26 - Vulnerability reported to vendor
- 2019-10-10 - Coordinated public release of advisory
- 2020-01-06 - Advisory Updated
