# ZDI-16-013: Adobe Reader DC Forms Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-013
- **ZDI-CAN:** ZDI-CAN-3265
- **Date:** 2016-01-12
- **CVE:** CVE-2016-0938
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Jaanus Kp Clarified Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-013/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the AcroForm plugin. A specially crafted PDF file can force Adobe Reader DC to read memory past the end of an allocated object. An attacker could leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb16-02.html

## Disclosure Timeline

- 2015-09-15 - Vulnerability reported to vendor
- 2016-01-12 - Coordinated public release of advisory
