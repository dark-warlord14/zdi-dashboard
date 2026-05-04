# ZDI-20-1423: NETGEAR Multiple Routers mini_httpd Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1423
- **ZDI-CAN:** ZDI-CAN-11653
- **Date:** 2020-12-21
- **CVE:** CVE-2020-27867
- **CVSS:** 6.8
- **CVSS Vector:** AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** Multiple Routers
- **Credit:** 1sd3d
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1423/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR R6020, R6080, R6120, R6220, R6260, R6700v2, R6800, R6900v2, R7450, JNR3210, WNR2020, Nighthawk AC2100, and Nighthawk AC2400 routers. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the mini_httpd service, which listens on TCP port 80 by default. When parsing the funjsq_access_token parameter, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000062641/Security-Advisory-for-Password-Recovery-Vulnerabilities-on-Some-Routers

## Disclosure Timeline

- 2020-08-19 - Vulnerability reported to vendor
- 2020-12-21 - Coordinated public release of advisory
- 2020-12-21 - Advisory Updated
