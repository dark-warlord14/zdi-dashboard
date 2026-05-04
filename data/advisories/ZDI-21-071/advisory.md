# ZDI-21-071: NETGEAR R7450 Password Recovery External Control of Critical State Data Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-071
- **ZDI-CAN:** ZDI-CAN-11365
- **Date:** 2021-01-18
- **CVE:** CVE-2020-27872
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** R7450
- **Credit:** 1sd3d of Viettel Cyber Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-071/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of NETGEAR R7450 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the mini_httpd service, which listens on TCP port 80 by default. The issue results from improper state tracking in the password recovery process. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000062641/Security-Advisory-for-Password-Recovery-Vulnerabilities-on-Some-Routers

## Disclosure Timeline

- 2020-08-21 - Vulnerability reported to vendor
- 2021-01-18 - Coordinated public release of advisory
