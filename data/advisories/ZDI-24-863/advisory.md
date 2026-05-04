# ZDI-24-863: (Pwn2Own) Phoenix Contact CHARX SEC-3100 plctool Improper Privilege Management Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-863
- **ZDI-CAN:** ZDI-CAN-23305
- **Date:** 2024-06-21
- **CVE:** CVE-2024-26002
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Phoenix Contact
- **Affected Products:** CHARX SEC-3100
- **Credit:** Midnight Blue / PHP Hooligans
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-863/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Phoenix Contact CHARX SEC-3100 devices. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the plctool binary. The binary can be abused to set incorrect permissions on files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Phoenix Contact has issued an update to correct this vulnerability. More details can be found at: https://cert.vde.com/en/advisories/VDE-2024-011/

## Disclosure Timeline

- 2024-02-02 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
