# ZDI-24-1727: (0Day) Panda Security Dome Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1727
- **ZDI-CAN:** ZDI-CAN-23478
- **Date:** 2024-12-30
- **CVE:** CVE-2024-13043
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Panda Security
- **Affected Products:** Dome
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1727/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Panda Security Dome. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Hotspot Shield. By creating a junction, an attacker can abuse the application to delete arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

07/12/24 – ZDI reported the vulnerability to the vendor 11/19/24 - ZDI asked for updates 11/20/24 – the vendor acknowledged the reported issue 12/16/24 - ZDI asked for updates 12/17/24 - ZDI notified the vendor of the intention to publish the case as 0-day advisory Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application

## Disclosure Timeline

- 2024-07-12 - Vulnerability reported to vendor
- 2024-12-30 - Coordinated public release of advisory
- 2024-12-30 - Advisory Updated
