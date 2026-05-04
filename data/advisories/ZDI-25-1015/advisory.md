# ZDI-25-1015: Parallels Toolbox CleanDrive Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1015
- **ZDI-CAN:** ZDI-CAN-26516
- **Date:** 2025-11-25
- **CVE:** CVE-2025-66288
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Parallels
- **Affected Products:** Toolbox
- **Credit:** Zeze with TeamT5
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1015/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Toolbox. An attacker must first obtain the ability to execute low-privileged code on the target host system in order to exploit this vulnerability. Additional user interaction is required in that an administrator must begin a cleanup of temporary files on the system. The specific flaw exists within the CleanDrive service. By creating a symbolic link, an attacker can abuse the service to delete arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Fixed in Parallels Toolbox for Windows versions 7.1.1

## Disclosure Timeline

- 2025-03-19 - Vulnerability reported to vendor
- 2025-11-25 - Coordinated public release of advisory
- 2025-12-03 - Advisory Updated
