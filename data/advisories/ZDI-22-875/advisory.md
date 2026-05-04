# ZDI-22-875: ABB e-Design Link Following Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-875
- **ZDI-CAN:** ZDI-CAN-16322
- **Date:** 2022-06-29
- **CVE:** CVE-2022-28702
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** ABB
- **Affected Products:** e-Design
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-875/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of ABB e-Design. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the installer. By creating a symbolic link, an attacker can abuse the installer to create a file. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

ABB has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-179-01

## Disclosure Timeline

- 2022-01-26 - Vulnerability reported to vendor
- 2022-06-29 - Coordinated public release of advisory
