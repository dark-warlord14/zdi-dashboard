# ZDI-22-317: Microsoft Windows User Profile Picture Link Following Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-317
- **ZDI-CAN:** ZDI-CAN-15296
- **Date:** 2022-02-11
- **CVE:** CVE-2022-22002
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Abdelhamid Naceri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-317/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the UserTileBroker component. By creating a symbolic link, an attacker can abuse the component to create a file. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-22002

## Disclosure Timeline

- 2021-10-27 - Vulnerability reported to vendor
- 2022-02-11 - Coordinated public release of advisory
