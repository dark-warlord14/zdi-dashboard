# ZDI-26-271: Avast Premium Security Gen Self Protection Driver Exposed Dangerous Function Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-271
- **ZDI-CAN:** ZDI-CAN-29388
- **Date:** 2026-04-15
- **CVE:** CVE-2026-5424
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Avast
- **Affected Products:** Premium Security
- **Credit:** aviel zohar
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-271/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Avast Premium Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Gen Self Protection driver. The issue results from an exposed dangerous function. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Fixed in version 26.3

## Disclosure Timeline

- 2026-04-01 - Vulnerability reported to vendor
- 2026-04-15 - Coordinated public release of advisory
- 2026-04-15 - Advisory Updated
