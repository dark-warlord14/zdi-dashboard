# ZDI-25-988: MSP360 Free Backup Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-988
- **ZDI-CAN:** ZDI-CAN-27245
- **Date:** 2025-11-11
- **CVE:** CVE-2025-12838
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** MSP360
- **Affected Products:** Free Backup
- **Credit:** Sharkkcode and Zeze with TeamT5
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-988/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of MSP360 Free Backup. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. User interaction on the part of an administrator is needed additionally. The specific flaw exists within the restore functionality. By creating a junction, an attacker can abuse the service to create arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Fixed in version 8.1.4

## Disclosure Timeline

- 2025-06-18 - Vulnerability reported to vendor
- 2025-11-11 - Coordinated public release of advisory
- 2025-11-11 - Advisory Updated
