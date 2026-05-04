# ZDI-24-558: G DATA Total Security Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-558
- **ZDI-CAN:** ZDI-CAN-22313
- **Date:** 2024-05-31
- **CVE:** CVE-2024-1868
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** G DATA
- **Affected Products:** Total Security
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-558/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of G DATA Total Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the G DATA Backup Service. By creating a symbolic link, an attacker can abuse the service to overwrite a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Fixed in version (25.5.17.355)

## Disclosure Timeline

- 2024-01-09 - Vulnerability reported to vendor
- 2024-05-31 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
