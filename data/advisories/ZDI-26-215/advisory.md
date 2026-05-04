# ZDI-26-215: KeePassXC OpenSSL Configuration Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-215
- **ZDI-CAN:** ZDI-CAN-29156
- **Date:** 2026-03-16
- **CVE:** CVE-2026-4158
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** KeePassXC
- **Affected Products:** KeePassXC
- **Credit:** Xavier DANEST
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-215/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of KeePassXC. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the configuration of OpenSSL. The product loads configuration from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of KeePassXC when run by a target user on the system.

## Additional Details

KeePassXC has issued an update to correct this vulnerability. More details can be found at: https://github.com/keepassxreboot/keepassxc/security/advisories/GHSA-4gr2-cr97-q9fx

## Disclosure Timeline

- 2026-03-03 - Vulnerability reported to vendor
- 2026-03-16 - Coordinated public release of advisory
- 2026-03-16 - Advisory Updated
