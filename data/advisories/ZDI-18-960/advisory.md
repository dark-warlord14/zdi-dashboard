# ZDI-18-960: Adobe Acrobat Pro DC U3D TIFF Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-960
- **ZDI-CAN:** ZDI-CAN-5995
- **Date:** 2018-08-30
- **CVE:** CVE-2018-5044
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-960/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of TIFF images from U3D objects. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb18-21.html

## Disclosure Timeline

- 2018-04-25 - Vulnerability reported to vendor
- 2018-08-30 - Coordinated public release of advisory
- 2018-09-12 - Advisory Updated
