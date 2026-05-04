# ZDI-22-538: (0Day) Epic Games Launcher Link Following Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-538
- **ZDI-CAN:** ZDI-CAN-14615
- **Date:** 2022-03-24
- **CVE:** N/A
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Epic Games
- **Affected Products:** Epic Games Launcher
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-538/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Epic Games Launcher. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Epic Games installer. By creating a symbolic link, an attacker can abuse the installer to delete a file. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 08/11/21 – ZDI reported the vulnerabilities to vendor 02/22/22 – ZDI requested an update 03/16/22 – ZDI notified the vendor of the intention to publish the cases as 0-day advisories on 03/24/22 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-08-27 - Vulnerability reported to vendor
- 2022-03-24 - Coordinated public release of advisory
- 2022-03-29 - Advisory Updated
