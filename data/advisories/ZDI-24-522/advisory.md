# ZDI-24-522: (Pwn2Own) Phoenix Contact CHARX SEC-3100 Filename Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-522
- **ZDI-CAN:** ZDI-CAN-23330
- **Date:** 2024-05-29
- **CVE:** CVE-2024-28135
- **CVSS:** 6.8
- **CVSS Vector:** AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Phoenix Contact
- **Affected Products:** CHARX SEC-3100
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-522/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Phoenix Contact CHARX SEC-3100 devices. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of the filename parameter to the update2-install endpoint. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the user-app account.

## Additional Details

Phoenix Contact has issued an update to correct this vulnerability. More details can be found at: https://cert.vde.com/en/advisories/VDE-2024-019/

## Disclosure Timeline

- 2024-02-21 - Vulnerability reported to vendor
- 2024-05-29 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
