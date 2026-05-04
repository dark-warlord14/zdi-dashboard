# ZDI-21-262: (Pwn2Own) NETGEAR R7800 apply_save.cgi rc_service Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-262
- **ZDI-CAN:** ZDI-CAN-12355
- **Date:** 2021-02-26
- **CVE:** CVE-2021-27256
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** R7800
- **Credit:** takeshi
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-262/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR R7800. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of the rc_service parameter provided to apply_save.cgi. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000062883/Security-Advisory-for-Multiple-Vulnerabilities-on-Some-Routers-Satellites-and-Extenders

## Disclosure Timeline

- 2020-12-31 - Vulnerability reported to vendor
- 2021-02-26 - Coordinated public release of advisory
