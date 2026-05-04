# ZDI-23-1161: NETGEAR RAX30 UPnP Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1161
- **ZDI-CAN:** ZDI-CAN-19704
- **Date:** 2023-08-22
- **CVE:** CVE-2023-40479
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** RAX30
- **Credit:** Kevin Wang
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1161/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR RAX30 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the UPnP service. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000065645/Security-Advisory-for-Multiple-Vulnerabilities-on-the-RAX30-PSV-2022-0360-PSV-2022-0361

## Disclosure Timeline

- 2022-12-28 - Vulnerability reported to vendor
- 2023-08-22 - Coordinated public release of advisory
