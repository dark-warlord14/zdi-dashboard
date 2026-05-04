# ZDI-25-1017: ASUS MyASUS Incorrect Permission Assignment Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1017
- **ZDI-CAN:** ZDI-CAN-27794
- **Date:** 2025-11-25
- **CVE:** CVE-2025-59373
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** ASUS
- **Affected Products:** MyASUS
- **Credit:** GuYongZeng @0x0dee
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1017/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of ASUS MyASUS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the AsusSwitchAgent component. The issue results from incorrect permissions on a named pipe. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Fixed in ASUS System Control Interface 3.1.48.0 (x64) and ASUS System Control Interface 4.2.48.0 (ARM): https://www.asus.com/security-advisory

## Disclosure Timeline

- 2025-08-26 - Vulnerability reported to vendor
- 2025-11-25 - Coordinated public release of advisory
- 2025-11-25 - Advisory Updated
