# ZDI-18-186: Adobe Reader DC XFA dashDot Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-186
- **ZDI-CAN:** ZDI-CAN-5258
- **Date:** 2018-02-23
- **CVE:** CVE-2018-4888
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Sebastian Apelt siberas
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-186/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of XFA forms in PDF documents. A crafted dashDot attribute in an XFA form can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb18-02.html

## Disclosure Timeline

- 2017-10-26 - Vulnerability reported to vendor
- 2018-02-23 - Coordinated public release of advisory
- 2018-02-23 - Advisory Updated
