# ZDI-25-338: Adobe Acrobat Reader DC Collab Object Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-338
- **ZDI-CAN:** ZDI-CAN-26593
- **Date:** 2025-06-10
- **CVE:** CVE-2025-43574
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Mark Vincent Yason (markyason.github.io)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-338/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Collab objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb25-57.html

## Disclosure Timeline

- 2025-03-05 - Vulnerability reported to vendor
- 2025-06-10 - Coordinated public release of advisory
- 2025-06-10 - Advisory Updated
