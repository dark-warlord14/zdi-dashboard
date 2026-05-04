# ZDI-24-1159: G DATA Total Security Scan Server Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1159
- **ZDI-CAN:** ZDI-CAN-23381
- **Date:** 2024-08-22
- **CVE:** CVE-2024-30377
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** G DATA
- **Affected Products:** Total Security
- **Credit:** Naor Hodorov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1159/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of G DATA Total Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the G DATA AntiVirus Scan Server. By creating a symbolic link, an attacker can abuse the service to delete arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Fixed in version 25.5.18.333

## Disclosure Timeline

- 2024-03-08 - Vulnerability reported to vendor
- 2024-08-22 - Coordinated public release of advisory
- 2024-12-11 - Advisory Updated
