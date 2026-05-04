# ZDI-21-286: Microsoft Windows Update Agent Directory Junction Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-286
- **ZDI-CAN:** ZDI-CAN-12442
- **Date:** 2021-03-15
- **CVE:** CVE-2021-26866
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Abdelhamid Naceri (halov)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-286/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within Windows Update Agent. By creating a directory junction, an attacker can abuse Windows Update Agent to delete a directory. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-26866

## Disclosure Timeline

- 2020-12-04 - Vulnerability reported to vendor
- 2021-03-15 - Coordinated public release of advisory
