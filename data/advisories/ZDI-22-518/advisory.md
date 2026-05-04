# ZDI-22-518: (Pwn2Own) NETGEAR R6700v3 httpd Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-518
- **ZDI-CAN:** ZDI-CAN-15854
- **Date:** 2022-03-23
- **CVE:** CVE-2022-27642
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** NETGEAR
- **Affected Products:** R6700v3
- **Credit:** Bugscale team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-518/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of NETGEAR R6700v3 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the httpd service. The issue results from incorrect string matching logic when accessing protected pages. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000064723/Security-Advisory-for-Multiple-Vulnerabilities-on-Multiple-Products-PSV-2021-0327

## Disclosure Timeline

- 2021-12-01 - Vulnerability reported to vendor
- 2022-03-23 - Coordinated public release of advisory
