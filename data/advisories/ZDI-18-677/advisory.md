# ZDI-18-677: Adobe Acrobat Pro DC JPEG2000 Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-677
- **ZDI-CAN:** ZDI-CAN-6341
- **Date:** 2018-07-16
- **CVE:** CVE-2018-12790
- **CVSS:** 2.6
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** Pengsu Cheng of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-677/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Adobe Acrobat Pro DC and Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the JPEG2000 core library. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb18-21.html

## Disclosure Timeline

- 2018-06-05 - Vulnerability reported to vendor
- 2018-07-16 - Coordinated public release of advisory
- 2018-07-16 - Advisory Updated
