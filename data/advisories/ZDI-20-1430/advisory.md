# ZDI-20-1430: NETGEAR Orbi UA_Parser Host Name Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1430
- **ZDI-CAN:** ZDI-CAN-11076
- **Date:** 2020-12-15
- **CVE:** CVE-2020-27861
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** Orbi
- **Credit:** Shaunak Mirani
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1430/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR Orbi routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the UA_Parser utility. A crafted Host Name option in a DHCP request can trigger execution of a system call composed from a user-supplied string. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000062507/Security-Advisory-for-Unauthenticated-Command-Injection-Vulnerability-on-Some-Extenders-and-Orbi-WiFi-Systems

## Disclosure Timeline

- 2020-07-10 - Vulnerability reported to vendor
- 2020-12-15 - Coordinated public release of advisory
