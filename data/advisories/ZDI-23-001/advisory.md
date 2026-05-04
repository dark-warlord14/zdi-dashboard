# ZDI-23-001: Microsoft Windows Installer Service Time-Of-Check Time-Of-Use Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-001
- **ZDI-CAN:** ZDI-CAN-18151
- **Date:** 2023-01-18
- **CVE:** CVE-2023-21542
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** QueryX Team of Theori
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-001/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Windows Installer service. By creating a junction, an attacker can abuse the service to create files in an arbitrary folder. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21542

## Disclosure Timeline

- 2022-08-31 - Vulnerability reported to vendor
- 2023-01-18 - Coordinated public release of advisory
