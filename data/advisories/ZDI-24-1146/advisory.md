# ZDI-24-1146: Microsoft Windows 10 WinREUpdateInstaller DLL Hijacking Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1146
- **ZDI-CAN:** ZDI-CAN-23934
- **Date:** 2024-08-13
- **CVE:** CVE-2024-38163
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Nicholas Zubrisky (@NZubrisky)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1146/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the WinREUpdateInstaller installer. The process does not restrict DLL search to trusted paths, which can result in the loading of a malicious DLL. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38163

## Disclosure Timeline

- 2024-04-12 - Vulnerability reported to vendor
- 2024-08-13 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
