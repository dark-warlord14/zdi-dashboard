# ZDI-23-503: (Pwn2Own) NETGEAR RAX30 logCtrl Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-503
- **ZDI-CAN:** ZDI-CAN-19825
- **Date:** 2023-05-01
- **CVE:** CVE-2023-27356
- **CVSS:** 6.8
- **CVSS Vector:** AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** RAX30
- **Credit:** Interrupt Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-503/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR RAX30 routers. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the logCtrl action. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000065618/Security-Advisory-for-Post-authentication-Command-Injection-on-Some-Routers-PSV-2022-0350

## Disclosure Timeline

- 2023-01-26 - Vulnerability reported to vendor
- 2023-05-01 - Coordinated public release of advisory
