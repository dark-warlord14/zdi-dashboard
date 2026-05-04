# ZDI-21-1051: NETGEAR Multiple Routers mini_httpd Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1051
- **ZDI-CAN:** ZDI-CAN-13313
- **Date:** 2021-08-30
- **CVE:** CVE-2021-34865
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** Multiple Routers
- **Credit:** 1sd3d of VCS
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1051/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of multiple NETGEAR routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the mini_httpd service, which listens on TCP port 80 by default. The issue results from incorrect string matching logic when accessing protected pages. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000063955/Security-Advisory-for-Authentication-Bypass-Vulnerability-on-Some-Routers-PSV-2021-0083?article=000063955

## Disclosure Timeline

- 2021-04-28 - Vulnerability reported to vendor
- 2021-08-30 - Coordinated public release of advisory
