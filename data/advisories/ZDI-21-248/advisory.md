# ZDI-21-248: (Pwn2Own) NETGEAR R7800 udchpd DHCP_REQUEST Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-248
- **ZDI-CAN:** ZDI-CAN-12216
- **Date:** 2021-02-24
- **CVE:** CVE-2021-27252
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** R7800
- **Credit:** atdog (@atdog_tw)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-248/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR R7800. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the vendor_specific DHCP opcode. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000062883/Security-Advisory-for-Multiple-Vulnerabilities-on-Some-Routers-Satellites-and-Extenders

## Disclosure Timeline

- 2020-11-05 - Vulnerability reported to vendor
- 2021-02-24 - Coordinated public release of advisory
