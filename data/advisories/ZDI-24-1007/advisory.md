# ZDI-24-1007: AVG AntiVirus Free AVGSvc Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1007
- **ZDI-CAN:** ZDI-CAN-22960
- **Date:** 2024-07-29
- **CVE:** CVE-2024-7237
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** AVG
- **Affected Products:** AntiVirus Free
- **Credit:** Nicholas Zubrisky (@NZubrisky) and Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1007/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of AVG AntiVirus Free. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the AVG Service. By creating a symbolic link, an attacker can abuse the service to delete a folder. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Fixed in Feb 24 Firmware Version 24.Xx

## Disclosure Timeline

- 2024-01-03 - Vulnerability reported to vendor
- 2024-07-29 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
