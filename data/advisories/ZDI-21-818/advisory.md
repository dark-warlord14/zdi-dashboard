# ZDI-21-818: Microsoft Windows InstallService Time-Of-Check Time-Of-Use Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-818
- **ZDI-CAN:** ZDI-CAN-12925
- **Date:** 2021-07-19
- **CVE:** CVE-2021-31961
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** JeongOh Kyea (@kkokkokye) of THEORI
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-818/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Microsoft Store Install Service. The issue results from the lack of proper locking when performing operations on a file. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-31961

## Disclosure Timeline

- 2021-02-08 - Vulnerability reported to vendor
- 2021-07-19 - Coordinated public release of advisory
