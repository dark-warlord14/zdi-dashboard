# ZDI-25-135: Adobe Acrobat Reader DC AcroForm Use of Uninitialized Variable Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-135
- **ZDI-CAN:** ZDI-CAN-26232
- **Date:** 2025-03-13
- **CVE:** CVE-2025-27162
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Mark Vincent Yason (markyason.github.io)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-135/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of AcroForms. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb25-14.html

## Disclosure Timeline

- 2025-02-07 - Vulnerability reported to vendor
- 2025-03-13 - Coordinated public release of advisory
- 2025-03-13 - Advisory Updated
