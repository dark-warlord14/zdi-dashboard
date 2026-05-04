# ZDI-20-124: Microsoft Windows Device Management Enrollment Service Hard Link Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-124
- **ZDI-CAN:** ZDI-CAN-9377
- **Date:** 2020-01-15
- **CVE:** CVE-2020-0616
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:N/I:L/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Jeong Oh Kyea(@kkokkokye) of THEORI
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-124/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Device Management Enrollment Service. By creating a hard link, an attacker can abuse the service to overwrite the contents of a chosen file. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0616

## Disclosure Timeline

- 2019-10-03 - Vulnerability reported to vendor
- 2020-01-15 - Coordinated public release of advisory
