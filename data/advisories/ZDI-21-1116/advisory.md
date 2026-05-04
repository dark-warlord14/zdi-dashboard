# ZDI-21-1116: NETGEAR R7800 net-cgi Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1116
- **ZDI-CAN:** ZDI-CAN-13055
- **Date:** 2021-09-28
- **CVE:** CVE-2021-34947
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** R7800
- **Credit:** Hoang Thach Nguyen of STAR Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1116/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR R7800 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the parsing of the soap_block_table file. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000064044/Security-Advisory-for-Pre-Authentication-Buffer-Overflow-on-Some-Routers-PSV-2021-0129

## Disclosure Timeline

- 2021-05-26 - Vulnerability reported to vendor
- 2021-09-28 - Coordinated public release of advisory
