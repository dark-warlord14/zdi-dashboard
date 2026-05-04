# ZDI-25-308: Adobe Dreamweaver V8 Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-308
- **ZDI-CAN:** ZDI-CAN-25684
- **Date:** 2025-05-21
- **CVE:** CVE-2025-30310
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Dreamweaver
- **Credit:** AspiringYoungMan
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-308/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Dreamweaver. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the JavaScript engine. The issue results from the use of a vulnerable version of V8. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/dreamweaver/apsb25-35.html

## Disclosure Timeline

- 2024-12-11 - Vulnerability reported to vendor
- 2025-05-21 - Coordinated public release of advisory
- 2025-05-21 - Advisory Updated
