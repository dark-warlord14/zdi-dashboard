# ZDI-19-803: Microsoft Windows AppX Deployment Service Junction Arbitrary File Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-803
- **ZDI-CAN:** ZDI-CAN-8602
- **Date:** 2019-09-10
- **CVE:** CVE-2019-1253
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Nabeel Ahmed of Dimension Data Belgium
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-803/
## Vulnerability Details

This vulnerability allows local attackers to delete arbitrary files on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the AppX Deployment Service. By creating a junction, an attacker can abuse the service to delete files in an incorrect location. An attacker can leverage this vulnerability to delete files in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1253

## Disclosure Timeline

- 2019-05-08 - Vulnerability reported to vendor
- 2019-09-10 - Coordinated public release of advisory
