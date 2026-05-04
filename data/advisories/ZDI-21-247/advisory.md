# ZDI-21-247: (Pwn2Own) NETGEAR Nighthawk R7800 ready-genie-cloud Insecure Download of Critical Component Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-247
- **ZDI-CAN:** ZDI-CAN-12308
- **Date:** 2021-02-24
- **CVE:** CVE-2021-27251
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** R7800
- **Credit:** Team FLASHBACK: Pedro Ribeiro (@pedrib1337 | pedrib@gmail.com) + Radek Domanski (@RabbitPro)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-247/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR Nighthawk R7800. Authentication is not required to exploit this vulnerability The specific flaw exists within handling of firmware updates. The issue results from a fallback to a insecure protocol to deliver updates. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000062883/Security-Advisory-for-Multiple-Vulnerabilities-on-Some-Routers-Satellites-and-Extenders

## Disclosure Timeline

- 2020-11-05 - Vulnerability reported to vendor
- 2021-02-24 - Coordinated public release of advisory
- 2021-02-24 - Advisory Updated
