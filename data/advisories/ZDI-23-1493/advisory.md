# ZDI-23-1493: G DATA Total Security GDBackupSvc Service Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1493
- **ZDI-CAN:** ZDI-CAN-20694
- **Date:** 2023-09-29
- **CVE:** CVE-2023-42126
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** G DATA
- **Affected Products:** Total Security
- **Credit:** Filip Dragovic (@filip_dragovic)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1493/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of G Data Total Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the GDBackupSvc service. By creating a symbolic link, an attacker can abuse the service to create a file with a permissive DACL. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Fixed in version 25.5.16.125

## Disclosure Timeline

- 2023-04-28 - Vulnerability reported to vendor
- 2023-09-29 - Coordinated public release of advisory
- 2023-12-07 - Advisory Updated
