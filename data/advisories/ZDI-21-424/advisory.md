# ZDI-21-424: Microsoft Windows AppX Deployment Service Directory Junction Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-424
- **ZDI-CAN:** ZDI-CAN-12445
- **Date:** 2021-04-21
- **CVE:** CVE-2021-28326
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Abdelhamid Naceri (halov)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-424/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the AppX Deployment Service. By creating a directory junction, an attacker can abuse the service to delete the contents of a chosen directory. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-28326

## Disclosure Timeline

- 2021-01-05 - Vulnerability reported to vendor
- 2021-04-21 - Coordinated public release of advisory
