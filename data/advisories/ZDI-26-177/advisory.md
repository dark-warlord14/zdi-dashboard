# ZDI-26-177: Array Networks MotionPro ArrayInstallManager Incorrect Permission Assignment Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-177
- **ZDI-CAN:** ZDI-CAN-26850
- **Date:** 2026-03-10
- **CVE:** CVE-2026-26364
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Array Networks
- **Affected Products:** MotionPro
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-177/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Array Networks MotionPro. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the ArrayInstallManager DCOM application. The issue results from incorrect permissions on the application. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Fixed in MotionPro version 1.2.28 https://support.arraynetworks.net/prx/000/http/supportportal.arraynetworks.net/downloads/downloads.html

## Disclosure Timeline

- 2025-05-21 - Vulnerability reported to vendor
- 2026-03-10 - Coordinated public release of advisory
- 2026-03-10 - Advisory Updated
