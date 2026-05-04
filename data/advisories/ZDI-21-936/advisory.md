# ZDI-21-936: Microsoft Edge Installer Directory Junction Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-936
- **ZDI-CAN:** ZDI-CAN-13799
- **Date:** 2021-08-03
- **CVE:** CVE-2021-36928
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** Abdelhamid Naceri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-936/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Edge. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within Edge Installer. By creating a directory junction, an attacker can abuse Edge Installer to delete a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-36928

## Disclosure Timeline

- 2021-06-08 - Vulnerability reported to vendor
- 2021-08-03 - Coordinated public release of advisory
