# ZDI-21-1078: Microsoft Windows Installer Service Directory Junction Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1078
- **ZDI-CAN:** ZDI-CAN-13762
- **Date:** 2021-09-16
- **CVE:** CVE-2021-36961
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Abdelhamid Naceri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1078/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Windows Installer Service. By creating a directory junction, an attacker can abuse the service to create a directory. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-36961

## Disclosure Timeline

- 2021-06-04 - Vulnerability reported to vendor
- 2021-09-16 - Coordinated public release of advisory
