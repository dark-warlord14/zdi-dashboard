# ZDI-19-975: Microsoft Windows UAC Unsafe Interaction Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-975
- **ZDI-CAN:** ZDI-CAN-9022
- **Date:** 2019-11-13
- **CVE:** CVE-2019-1388
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Eduardo Braun Prado
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-975/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to access an interactive desktop as a low-privileged user on the target system in order to exploit this vulnerability. The specific flaw exists within the User Account Control (UAC) user interface shown on the secure desktop. By interacting with the user interface, an attacker can launch a highly-privileged web browser on the normal desktop. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1388

## Disclosure Timeline

- 2019-07-23 - Vulnerability reported to vendor
- 2019-11-13 - Coordinated public release of advisory
