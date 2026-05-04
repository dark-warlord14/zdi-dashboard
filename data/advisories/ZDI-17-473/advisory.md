# ZDI-17-473: (Pwn2Own) Microsoft Windows PlgBlt Integer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-473
- **ZDI-CAN:** ZDI-CAN-4624
- **Date:** 2017-07-11
- **CVE:** CVE-2017-8578
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Tencent Security - Team Sniper (Keen Lab and PC Mgr)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-473/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the implementation of PlgBlt, an operation that writes bitmap graphics to parallelogram-shaped destination areas. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before writing to memory. An attacker can leverage this vulnerability to escalate privilege to the level of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-8578

## Disclosure Timeline

- 2017-03-16 - Vulnerability reported to vendor
- 2017-07-11 - Coordinated public release of advisory
