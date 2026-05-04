# ZDI-20-281: Microsoft Windows AppX Deployment Service Hard Link Escalation of Privilege Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-281
- **ZDI-CAN:** ZDI-CAN-9502
- **Date:** 2020-03-12
- **CVE:** CVE-2020-0840
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** JeongOh Kyea(@kkokkokye) of THEORI
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-281/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the AppX Deployment Service. By creating a hard link, an attacker can abuse the service to overwrite the contents of a chosen file. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0840

## Disclosure Timeline

- 2019-11-28 - Vulnerability reported to vendor
- 2020-03-12 - Coordinated public release of advisory
