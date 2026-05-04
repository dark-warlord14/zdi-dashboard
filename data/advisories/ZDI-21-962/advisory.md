# ZDI-21-962: Microsoft Windows Defender Directory Junction Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-962
- **ZDI-CAN:** ZDI-CAN-13504
- **Date:** 2021-08-11
- **CVE:** CVE-2021-34471
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Abdelhamid Naceri (halov)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-962/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within Windows Defender. By creating a directory junction, an attacker can abuse Windows Defender to delete a file. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34471

## Disclosure Timeline

- 2021-05-05 - Vulnerability reported to vendor
- 2021-08-11 - Coordinated public release of advisory
