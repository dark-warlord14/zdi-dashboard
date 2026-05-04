# ZDI-24-363: Microsoft Windows Installer Service Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-363
- **ZDI-CAN:** ZDI-CAN-22924
- **Date:** 2024-04-09
- **CVE:** CVE-2024-26158
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Simon Zuckerbraun of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-363/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Windows Installer service. By creating a symbolic link, an attacker can abuse the service to write arbitrary registry values. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-26158

## Disclosure Timeline

- 2023-12-22 - Vulnerability reported to vendor
- 2024-04-09 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
