# ZDI-22-1131: Measuresoft ScadaPro Server Link Following Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1131
- **ZDI-CAN:** ZDI-CAN-16434
- **Date:** 2022-08-23
- **CVE:** CVE-2022-2898
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Measuresoft
- **Affected Products:** ScadaPro Server
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1131/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Measuresoft ScadaPro Server. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the ScadaPro Server installer. By creating a symbolic link, an attacker can abuse the installer to create a file. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Measuresoft has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-235-06

## Disclosure Timeline

- 2022-02-01 - Vulnerability reported to vendor
- 2022-08-23 - Coordinated public release of advisory
