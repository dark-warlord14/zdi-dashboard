# ZDI-20-282: Microsoft Windows DiagTrack Service Hard Link Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-282
- **ZDI-CAN:** ZDI-CAN-9691
- **Date:** 2020-03-12
- **CVE:** CVE-2020-0841
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** JeongOh Kyea(@kkokkokye) of THEORI
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-282/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the DiagTrack service. By creating a hard link, an attacker can abuse the service to overwrite a chosen file. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0841

## Disclosure Timeline

- 2019-11-28 - Vulnerability reported to vendor
- 2020-03-12 - Coordinated public release of advisory
