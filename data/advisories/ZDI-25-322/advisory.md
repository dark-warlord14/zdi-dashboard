# ZDI-25-322: 2BrightSparks SyncBackFree Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-322
- **ZDI-CAN:** ZDI-CAN-26962
- **Date:** 2025-06-03
- **CVE:** CVE-2025-5474
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** 2BrightSparks
- **Affected Products:** SyncBackFree
- **Credit:** Sharkkcode and Zeze with TeamT5
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-322/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of 2BrightSparks SyncBackFree. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. User interaction on the part of an administrator is also required. The specific flaw exists within the Mirror functionality. By creating a junction, an attacker can abuse the service to delete arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Fixed in SyncBack V11.3.106.0 https://www.2brightsparks.com/download-syncbackfree.html

## Disclosure Timeline

- 2025-05-13 - Vulnerability reported to vendor
- 2025-06-03 - Coordinated public release of advisory
- 2025-06-06 - Advisory Updated
