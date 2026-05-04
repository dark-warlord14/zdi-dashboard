# ZDI-22-874: ABB e-Design Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-874
- **ZDI-CAN:** ZDI-CAN-16278
- **Date:** 2022-06-29
- **CVE:** CVE-2022-29483
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** ABB
- **Affected Products:** e-Design
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-874/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of ABB e-Design. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the e-Design installer. By creating a symbolic link, an attacker can abuse the installer to delete a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

ABB has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-179-01

## Disclosure Timeline

- 2022-01-26 - Vulnerability reported to vendor
- 2022-06-29 - Coordinated public release of advisory
