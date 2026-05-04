# ZDI-25-323: Action1 Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-323
- **ZDI-CAN:** ZDI-CAN-26767
- **Date:** 2025-06-03
- **CVE:** CVE-2025-5480
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Action1
- **Affected Products:** Action1
- **Credit:** Xavier DANEST
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-323/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Action1. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the configuration of OpenSSL. The product loads an OpenSSL configuration file from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Action1 has issued an update to correct this vulnerability. More details can be found at: https://www.action1.com/blog/acknowledging-zdi-can-26767-high-severity-vulnerability-in-action1-agent/

## Disclosure Timeline

- 2025-04-28 - Vulnerability reported to vendor
- 2025-06-03 - Coordinated public release of advisory
- 2025-06-06 - Advisory Updated
