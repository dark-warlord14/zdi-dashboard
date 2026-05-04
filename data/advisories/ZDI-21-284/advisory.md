# ZDI-21-284: Microsoft Windows Setup Directory Junction Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-284
- **ZDI-CAN:** ZDI-CAN-12093
- **Date:** 2021-03-15
- **CVE:** CVE-2021-1729
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Abdelhamid Naceri (halov)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-284/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within Windows Setup. By creating a directory junction, an attacker can abuse Windows Setup to delete a file. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-1729

## Disclosure Timeline

- 2020-11-18 - Vulnerability reported to vendor
- 2021-03-15 - Coordinated public release of advisory
