# ZDI-23-913: Microsoft Windows Installer Service Time-Of-Check Time-Of-Use Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-913
- **ZDI-CAN:** ZDI-CAN-17704
- **Date:** 2023-07-12
- **CVE:** CVE-2023-32050
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** JeongOh Kyea of THEORI
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-913/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target host system in order to exploit this vulnerability. The specific flaw exists within the Windows Installer service. By creating a junction, an attacker can abuse the service to change permissions on an arbitrary file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-32050

## Disclosure Timeline

- 2022-07-22 - Vulnerability reported to vendor
- 2023-07-12 - Coordinated public release of advisory
