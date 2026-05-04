# ZDI-19-978: Microsoft Windows InstallService Hard Link Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-978
- **ZDI-CAN:** ZDI-CAN-9156
- **Date:** 2019-11-13
- **CVE:** CVE-2019-1423
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** kkokkokye@THEORI
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-978/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Microsoft Store Install Service. By creating a hard link, an attacker can abuse the service to overwrite the contents of a chosen file. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1423

## Disclosure Timeline

- 2019-08-08 - Vulnerability reported to vendor
- 2019-11-13 - Coordinated public release of advisory
