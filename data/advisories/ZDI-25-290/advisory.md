# ZDI-25-290: Rockwell Automation ThinManager ThinServer Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-290
- **ZDI-CAN:** ZDI-CAN-25727
- **Date:** 2025-05-13
- **CVE:** CVE-2025-3617
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Rockwell Automation
- **Affected Products:** ThinManager
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-290/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Rockwell Automation ThinManager. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the ThinServer component. By creating a symbolic link, an attacker can abuse the service to delete arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Rockwell Automation has issued an update to correct this vulnerability. More details can be found at: https://www.rockwellautomation.com/en-us/trust-center/security-advisories/advisory.SD1727.html

## Disclosure Timeline

- 2025-01-03 - Vulnerability reported to vendor
- 2025-05-13 - Coordinated public release of advisory
- 2025-05-21 - Advisory Updated
