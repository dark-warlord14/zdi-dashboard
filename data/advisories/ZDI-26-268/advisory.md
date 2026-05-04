# ZDI-26-268: Samsung MagicINFO 9 Server Incorrect Default Permissions Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-268
- **ZDI-CAN:** ZDI-CAN-28705
- **Date:** 2026-04-15
- **CVE:** CVE-2026-25203
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Samsung
- **Affected Products:** MagicINFO 9 Server
- **Credit:** Bobby Gould (@bobbygould5) of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-268/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Samsung MagicINFO 9 Server. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the product installer. The issue results from incorrect permissions on a folder used by the product. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Fixed in version 21.1091.1 - https://security.samsungtv.com/securityUpdates

## Disclosure Timeline

- 2025-12-16 - Vulnerability reported to vendor
- 2026-04-15 - Coordinated public release of advisory
- 2026-04-15 - Advisory Updated
