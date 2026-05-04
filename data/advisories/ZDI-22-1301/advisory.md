# ZDI-22-1301: Measuresoft ScadaPro Server Improper Access Control Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1301
- **ZDI-CAN:** ZDI-CAN-16729
- **Date:** 2022-09-26
- **CVE:** CVE-2022-3263
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Measuresoft
- **Affected Products:** ScadaPro Server
- **Credit:** @rgod777
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1301/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Measuresoft ScadaPro Server. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the ORCHESTRATOR Service. The product sets incorrect permissions on the service. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Measuresoft has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-265-01

## Disclosure Timeline

- 2022-06-01 - Vulnerability reported to vendor
- 2022-09-26 - Coordinated public release of advisory
