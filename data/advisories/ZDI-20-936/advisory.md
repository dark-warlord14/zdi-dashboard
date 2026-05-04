# ZDI-20-936: NETGEAR R6700 acsd Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-936
- **ZDI-CAN:** ZDI-CAN-9853
- **Date:** 2020-08-04
- **CVE:** CVE-2020-15635
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** R6700
- **Credit:** Pedro Ribeiro (@pedrib1337 | pedrib@gmail.com) and Radek Domanski (@RabbitPro | radek.domanski@gmail.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-936/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR R6700 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the acsd service, which listens on TCP port 5916 by default. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the admin user.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000062127/Security-Advisory-for-Pre-Authentication-Buffer-Overflow-on-R6700v3-PSV-2020-0202

## Disclosure Timeline

- 2020-04-22 - Vulnerability reported to vendor
- 2020-08-04 - Coordinated public release of advisory
