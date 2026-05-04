# ZDI-21-252: (Pwn2Own) NETGEAR Nighthawk R7800 Use of Hard-coded Password Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-252
- **ZDI-CAN:** ZDI-CAN-12287
- **Date:** 2021-02-25
- **CVE:** CVE-2021-27254
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** NETGEAR
- **Affected Products:** R7800
- **Credit:** 84c0
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-252/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of NETGEAR R7800. Authentication is not required to exploit this vulnerability. The specific flaw exists within the apply_save.cgi endpoint. This issue results from the use of hard-coded encryption key. An attacker can leverage this vulnerability to execute arbitrary code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000062883/Security-Advisory-for-Multiple-Vulnerabilities-on-Some-Routers-Satellites-and-Extenders

## Disclosure Timeline

- 2020-11-06 - Vulnerability reported to vendor
- 2021-02-25 - Coordinated public release of advisory
