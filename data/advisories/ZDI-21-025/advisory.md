# ZDI-21-025: Microsoft Windows AppX Deployment Service Directory Junction Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-025
- **ZDI-CAN:** ZDI-CAN-12170
- **Date:** 2021-01-14
- **CVE:** CVE-2021-1685
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** JeongOh Kyea (@kkokkokye) of THEORI
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-025/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the AppX Deployment Service. By creating a directory junction, an attacker can abuse the service to create files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-1685

## Disclosure Timeline

- 2020-10-30 - Vulnerability reported to vendor
- 2021-01-14 - Coordinated public release of advisory
