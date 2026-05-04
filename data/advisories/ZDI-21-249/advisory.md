# ZDI-21-249: (Pwn2Own) NETGEAR Nighthawk R7800 Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-249
- **ZDI-CAN:** ZDI-CAN-12303
- **Date:** 2021-02-24
- **CVE:** CVE-2021-27253
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** R7800
- **Credit:** Ho\xc3\xa0ng Th\xe1\xba\xa1ch Nguy\xe1\xbb\x85n, Lucas Tay
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-249/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR Nighthawk R7800. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of the rc_service parameter provided to apply_bind.cgi. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000062883/Security-Advisory-for-Multiple-Vulnerabilities-on-Some-Routers-Satellites-and-Extenders

## Disclosure Timeline

- 2020-11-05 - Vulnerability reported to vendor
- 2021-02-24 - Coordinated public release of advisory
