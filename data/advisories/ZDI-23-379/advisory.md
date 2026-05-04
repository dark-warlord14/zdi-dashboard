# ZDI-23-379: G DATA Total Security Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-379
- **ZDI-CAN:** ZDI-CAN-18749
- **Date:** 2023-04-05
- **CVE:** CVE-2023-27347
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** G DATA
- **Affected Products:** Total Security
- **Credit:** Dennis Herrmann (@dhn_)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-379/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of G Data Total Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the G DATA Backup Service. By creating a symbolic link, an attacker can abuse the service to create arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Fixed in version is 25.5.13.26

## Disclosure Timeline

- 2022-10-26 - Vulnerability reported to vendor
- 2023-04-05 - Coordinated public release of advisory
- 2023-12-07 - Advisory Updated
