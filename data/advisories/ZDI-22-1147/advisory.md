# ZDI-22-1147: Measuresoft ScadaPro Client Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1147
- **ZDI-CAN:** ZDI-CAN-16422
- **Date:** 2022-08-23
- **CVE:** CVE-2022-2897
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Measuresoft
- **Affected Products:** ScadaPro Client
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1147/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Measuresoft ScadaPro Client. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the ScadaPro Client installer. By creating a symbolic link, an attacker can abuse the installer to overwrite a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Measuresoft has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-235-06

## Disclosure Timeline

- 2022-02-01 - Vulnerability reported to vendor
- 2022-08-23 - Coordinated public release of advisory
