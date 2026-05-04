# ZDI-22-524: (Pwn2Own) NETGEAR R6700v3 libreadycloud.so Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-524
- **ZDI-CAN:** ZDI-CAN-15874
- **Date:** 2022-03-23
- **CVE:** CVE-2022-27647
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** R6700v3
- **Credit:** Bugscale team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-524/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR R6700v3 routers. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of the name or email field provided to libreadycloud.so. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000064723/Security-Advisory-for-Multiple-Vulnerabilities-on-Multiple-Products-PSV-2021-0327

## Disclosure Timeline

- 2021-12-01 - Vulnerability reported to vendor
- 2022-03-23 - Coordinated public release of advisory
