# ZDI-18-1374: Adobe Acrobat Pro DC ImageConversion XPS GSUB Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1374
- **ZDI-CAN:** ZDI-CAN-7039
- **Date:** 2018-12-12
- **CVE:** CVE-2018-15985
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** Pengsu Cheng of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1374/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of the CoolType component in the GSUB table in a font. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb18-41.html

## Disclosure Timeline

- 2018-08-02 - Vulnerability reported to vendor
- 2018-12-12 - Coordinated public release of advisory
