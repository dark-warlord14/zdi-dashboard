# ZDI-17-908: Adobe Acrobat Pro DC ImageConversion EMF EMR_COMMENT Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-908
- **ZDI-CAN:** ZDI-CAN-5219
- **Date:** 2017-11-14
- **CVE:** CVE-2017-16401
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** Ke Liu of Tencent's Xuanwu LAB
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-908/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of EMR_COMMENT records in EMF files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb17-36.html

## Disclosure Timeline

- 2017-09-26 - Vulnerability reported to vendor
- 2017-11-14 - Coordinated public release of advisory
