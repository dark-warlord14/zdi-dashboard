# ZDI-21-285: Microsoft Windows Installer Service Directory Junction Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-285
- **ZDI-CAN:** ZDI-CAN-12324
- **Date:** 2021-03-15
- **CVE:** CVE-2021-26862
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Abdelhamid Naceri (halov)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-285/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Windows Installer Service. By creating a directory junction, an attacker can abuse the service to create an arbitrary file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-26862

## Disclosure Timeline

- 2020-12-04 - Vulnerability reported to vendor
- 2021-03-15 - Coordinated public release of advisory
