# ZDI-25-905: Gen Digital CCleaner Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-905
- **ZDI-CAN:** ZDI-CAN-26474
- **Date:** 2025-09-23
- **CVE:** CVE-2025-3025
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Gen Digital
- **Affected Products:** CCleaner
- **Credit:** Zeze with TeamT5
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-905/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Gen Digital CCleaner. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. Some interaction on the part of an administrator is additionally required. The specific flaw exists within the Custom Clean functionality. By creating a junction, an attacker can abuse the service to delete arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Gen Digital has issued an update to correct this vulnerability. More details can be found at: https://www.gendigital.com/us/en/contact-us/security-advisories/

## Disclosure Timeline

- 2025-03-30 - Vulnerability reported to vendor
- 2025-09-23 - Coordinated public release of advisory
- 2025-09-23 - Advisory Updated
