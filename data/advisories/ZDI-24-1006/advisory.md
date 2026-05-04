# ZDI-24-1006: AVG AntiVirus Free Link Following Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1006
- **ZDI-CAN:** ZDI-CAN-22803
- **Date:** 2024-07-29
- **CVE:** CVE-2024-7235
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** AVG
- **Affected Products:** AntiVirus Free
- **Credit:** Nicholas Zubrisky (@NZubrisky) and Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1006/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of AVG AntiVirus Free. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the AVG Service. By creating a symbolic link, an attacker can abuse the service to create a folder. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Fixed in Feb 24 Firmware Version 24.Xx

## Disclosure Timeline

- 2023-12-08 - Vulnerability reported to vendor
- 2024-07-29 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
