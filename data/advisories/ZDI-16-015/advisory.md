# ZDI-16-015: Adobe Acrobat Reader DC Uninitialized Memory Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-015
- **ZDI-CAN:** ZDI-CAN-3264
- **Date:** 2016-01-12
- **CVE:** CVE-2016-0939
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Jaanus Kp Clarified Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-015/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of PDF files. By providing a malformed PDF file, an attacker can cause uninitialized memory to be dereferenced. An attacker could leverage this to execute arbitrary code under the context of the process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb16-02.html

## Disclosure Timeline

- 2015-09-24 - Vulnerability reported to vendor
- 2016-01-12 - Coordinated public release of advisory
