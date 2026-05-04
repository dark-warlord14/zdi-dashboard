# ZDI-20-935: NETGEAR R6700 httpd strtblupgrade Format String Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-935
- **ZDI-CAN:** ZDI-CAN-9755
- **Date:** 2020-08-04
- **CVE:** CVE-2020-15634
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** NETGEAR
- **Affected Products:** R6700
- **Credit:** d4rkn3ss from VNPT ISC
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-935/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR R6700 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of string table file uploads. The issue results from the lack of proper validation of a user-supplied string before using it as a format specifier. An attacker can leverage this vulnerability to execute code in the context of the web server.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000062126/Security-Advisory-for-Pre-Authentication-Command-Injection-on-R6700v3-PSV-2020-0189

## Disclosure Timeline

- 2020-04-08 - Vulnerability reported to vendor
- 2020-08-04 - Coordinated public release of advisory
