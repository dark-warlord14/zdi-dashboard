# ZDI-18-600: Adobe Acrobat Pro DC ImageConversion EMF Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-600
- **ZDI-CAN:** ZDI-CAN-6100
- **Date:** 2018-06-26
- **CVE:** CVE-2018-4901
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** willJ of Tencent PC Manager
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-600/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of EMF files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb18-02.html

## Disclosure Timeline

- 2018-04-25 - Vulnerability reported to vendor
- 2018-06-26 - Coordinated public release of advisory
- 2018-06-26 - Advisory Updated
