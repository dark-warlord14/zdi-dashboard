# ZDI-21-330: Microsoft Windows EFI Partition Incorrect Authorization Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-330
- **ZDI-CAN:** ZDI-CAN-12299
- **Date:** 2021-03-17
- **CVE:** CVE-2021-26892
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Abdelhamid Naceri (halov)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-330/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Windows kernel. The issue results from improper authorization logic when accessing files in the EFI partition. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-26892

## Disclosure Timeline

- 2020-12-09 - Vulnerability reported to vendor
- 2021-03-17 - Coordinated public release of advisory
