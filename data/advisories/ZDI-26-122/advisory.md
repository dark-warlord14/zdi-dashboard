# ZDI-26-122: PDF-XChange Editor TrackerUpdate Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-122
- **ZDI-CAN:** ZDI-CAN-27788
- **Date:** 2026-02-19
- **CVE:** CVE-2026-2040
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** PDF-XChange
- **Affected Products:** PDF-XChange Editor
- **Credit:** Kolja Grassmann (Neodyme AG)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-122/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of PDF-XChange Editor. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the TrackerUpdate process. The product loads a library from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of a target user.

## Additional Details

Fixed in version 10.7.3.401 https://www.pdf-xchange.com/product/pdf-xchange-editor/history#10.7.3.401

## Disclosure Timeline

- 2025-09-16 - Vulnerability reported to vendor
- 2026-02-19 - Coordinated public release of advisory
- 2026-02-19 - Advisory Updated
