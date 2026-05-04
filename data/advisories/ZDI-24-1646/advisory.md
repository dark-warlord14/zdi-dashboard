# ZDI-24-1646: Epic Games Launcher Incorrect Default Permissions Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1646
- **ZDI-CAN:** ZDI-CAN-24329
- **Date:** 2024-12-04
- **CVE:** CVE-2024-11872
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Epic Games
- **Affected Products:** Epic Games Launcher
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1646/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Epic Games Launcher. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the product installer. The product applies incorrect default permissions to a sensitive folder. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Epic Games has issued an update to correct this vulnerability. More details can be found at: https://trello.com/c/tcS6Jcfy/578-epic-games-launcher-1720

## Disclosure Timeline

- 2024-07-16 - Vulnerability reported to vendor
- 2024-12-04 - Coordinated public release of advisory
- 2024-12-06 - Advisory Updated
