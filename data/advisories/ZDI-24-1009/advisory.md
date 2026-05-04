# ZDI-24-1009: AVG AntiVirus Free icarus Arbitrary File Creation Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1009
- **ZDI-CAN:** ZDI-CAN-22942
- **Date:** 2024-07-29
- **CVE:** CVE-2024-7236
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** AVG
- **Affected Products:** AntiVirus Free
- **Credit:** Nicholas Zubrisky (@NZubrisky) and Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1009/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of AVG AntiVirus Free. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the AVG Installer. By creating a symbolic link, an attacker can abuse the update functionality to create a file. An attacker can leverage this vulnerability to create a persistent denial-of-service condition on the system.

## Additional Details

Fixed in Feb 24 Firmware Version 24.Xx

## Disclosure Timeline

- 2024-02-22 - Vulnerability reported to vendor
- 2024-07-29 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
