# ZDI-16-324: Adobe Acrobat Pro DC ImageConversion JPEG Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-324
- **ZDI-CAN:** ZDI-CAN-3557
- **Date:** 2016-05-10
- **CVE:** CVE-2016-1076
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** AbdulAziz Hariri - HPE Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-324/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the ImageConversion plugin. A specially crafted JPEG image can force Adobe Acrobat Pro DC to read memory past the end of an allocated object. An attacker can use this information in conjunction with other vulnerabilities to execute code in the context of the process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb16-14.html

## Disclosure Timeline

- 2016-02-04 - Vulnerability reported to vendor
- 2016-05-10 - Coordinated public release of advisory
