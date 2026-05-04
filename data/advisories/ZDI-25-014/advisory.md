# ZDI-25-014: SonicWALL NSv setSshdConfig Exposed Dangerous Function Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-014
- **ZDI-CAN:** ZDI-CAN-24821
- **Date:** 2025-01-09
- **CVE:** CVE-2024-53706
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SonicWALL
- **Affected Products:** NSv
- **Credit:** Daan Keuper, Thijs Alkemade and Khaled Nassar of Computest Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-014/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of SonicWALL NSv. An attacker must first obtain the ability to execute low-privileged code on the target system or send a TCP packet to a local service in order to exploit this vulnerability. The specific flaw exists within the setSshdConfig command. The issue results from an exposed dangerous function. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

SonicWALL has issued an update to correct this vulnerability. More details can be found at: https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2025-0003

## Disclosure Timeline

- 2024-11-05 - Vulnerability reported to vendor
- 2025-01-09 - Coordinated public release of advisory
- 2025-01-09 - Advisory Updated
