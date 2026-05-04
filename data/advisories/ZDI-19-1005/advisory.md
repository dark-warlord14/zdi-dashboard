# ZDI-19-1005: Microsoft Windows AppX Deployment Service Hard Link Escalation of Privilege Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-1005
- **ZDI-CAN:** ZDI-CAN-9320
- **Date:** 2019-12-11
- **CVE:** CVE-2019-1483
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Jeong Oh Kyea(@kkokkokye) of THEORI
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-1005/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the AppX Deployment Service. By creating a hard link, an attacker can abuse the service to overwrite the contents of a chosen file. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1483

## Disclosure Timeline

- 2019-08-29 - Vulnerability reported to vendor
- 2019-12-11 - Coordinated public release of advisory
