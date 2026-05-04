# ZDI-20-288: (Pwn2Own) Xiaomi GetApps Intent Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-288
- **ZDI-CAN:** ZDI-CAN-9657
- **Date:** 2020-03-12
- **CVE:** CVE-2020-9531
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Xiaomi
- **Affected Products:** Mi6
- **Credit:** @FSecureLabs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-288/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Xiaomi GetApps. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of intents. The issue lies in the ability to send an intent that would not otherwise be permitted. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the application.

## Additional Details

Fixed in v 2001122

## Disclosure Timeline

- 2019-11-07 - Vulnerability reported to vendor
- 2020-03-12 - Coordinated public release of advisory
