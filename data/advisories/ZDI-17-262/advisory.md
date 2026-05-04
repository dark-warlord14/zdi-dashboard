# ZDI-17-262: Adobe Acrobat Pro DC ImageConversion PCX Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-262
- **ZDI-CAN:** ZDI-CAN-4395
- **Date:** 2017-04-11
- **CVE:** CVE-2017-3036
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** Ke Liu of Tencent's Xuanwu LAB
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-262/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within ImageConversion's PCX parsing. The issue results from the lack of proper validation of user-supplied data which can result in a write past the end of an allocated object. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb17-11.html

## Disclosure Timeline

- 2017-01-09 - Vulnerability reported to vendor
- 2017-04-11 - Coordinated public release of advisory
