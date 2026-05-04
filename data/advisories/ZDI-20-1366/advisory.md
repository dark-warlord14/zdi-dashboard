# ZDI-20-1366: Microsoft Windows Print Spooler Directory Junction Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1366
- **ZDI-CAN:** ZDI-CAN-11796
- **Date:** 2020-11-11
- **CVE:** CVE-2020-17014
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** JeongOh Kyea (@kkokkokye) of THEORI
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1366/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Print Spooler service. By creating a directory junction, an attacker can abuse the Print Spooler service to delete a file. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2020-17014

## Disclosure Timeline

- 2020-09-02 - Vulnerability reported to vendor
- 2020-11-11 - Coordinated public release of advisory
- 2020-12-01 - Advisory Updated
