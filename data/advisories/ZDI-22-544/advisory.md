# ZDI-22-544: (Pwn2Own) Netgear R6700v3 NetUSB Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-544
- **ZDI-CAN:** ZDI-CAN-15806
- **Date:** 2022-03-29
- **CVE:** CVE-2022-27641
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** R6700v3
- **Credit:** trichimtrich and nyancat0131
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-544/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR R6700v3 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the NetUSB module. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000064437/Security-Advisory-for-Pre-Authentication-Buffer-Overflow-on-Multiple-Products-PSV-2021-0278

## Disclosure Timeline

- 2021-12-01 - Vulnerability reported to vendor
- 2022-03-29 - Coordinated public release of advisory
