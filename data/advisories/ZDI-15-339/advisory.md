# ZDI-15-339: (Pwn2Own) Microsoft Windows Installer Local Elevation of Privilege Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-339
- **ZDI-CAN:** ZDI-CAN-2827
- **Date:** 2015-07-14
- **CVE:** CVE-2015-2371
- **CVSS:** 6.8
- **CVSS Vector:** AV:L/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Mariusz Mlynski
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-339/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code as SYSTEM on vulnerable installations of Microsoft Windows. An attacker must be logged in as a user on the system in order to execute the attack. The specific flaw exists within the behavior of some MSI installations. Some installations will launch an executable as SYSTEM during uninstallation or repair. The location of this executable is read from a registry key controllable by an unprivileged user, and because a repair operation does not require elevation, a standard user can use this functionality to execute arbitrary code as SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/MS15-074

## Disclosure Timeline

- 2015-03-18 - Vulnerability reported to vendor
- 2015-07-14 - Coordinated public release of advisory
