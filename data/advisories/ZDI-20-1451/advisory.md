# ZDI-20-1451: NETGEAR Multiple Routers mini_httpd Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1451
- **ZDI-CAN:** ZDI-CAN-11355
- **Date:** 2020-12-18
- **CVE:** CVE-2020-27866
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** Multiple Routers
- **Credit:** 1sd3d of Viettel Cyber Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1451/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of NETGEAR R6020, R6080, R6120, R6220, R6260, R6700v2, R6800, R6900v2, R7450, JNR3210, WNR2020, Nighthawk AC2100, and Nighthawk AC2400 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the mini_httpd service, which listens on TCP port 80 by default. The issue results from incorrect string matching logic when accessing protected pages. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000062641/Security-Advisory-for-Password-Recovery-Vulnerabilities-on-Some-Routers

## Disclosure Timeline

- 2020-08-19 - Vulnerability reported to vendor
- 2020-12-18 - Coordinated public release of advisory
