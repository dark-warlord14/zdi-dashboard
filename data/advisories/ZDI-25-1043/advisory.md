# ZDI-25-1043: Adobe Acrobat Reader DC Annotation Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1043
- **ZDI-CAN:** ZDI-CAN-27425
- **Date:** 2025-12-09
- **CVE:** CVE-2025-64899
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Mark Vincent Yason (markyason.github.io)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1043/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Annotation objects. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb25-119.html

## Disclosure Timeline

- 2025-06-26 - Vulnerability reported to vendor
- 2025-12-09 - Coordinated public release of advisory
- 2025-12-09 - Advisory Updated
