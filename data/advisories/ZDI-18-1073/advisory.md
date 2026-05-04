# ZDI-18-1073: Adobe Acrobat Pro DC HTML2PDF HTML Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1073
- **ZDI-CAN:** ZDI-CAN-5747
- **Date:** 2018-09-19
- **CVE:** CVE-2018-12775
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1073/
## Vulnerability Details

This vulnerability allows remote disclose sensitive information on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of HTML files in HTML2PDF. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb18-34.html

## Disclosure Timeline

- 2018-05-22 - Vulnerability reported to vendor
- 2018-09-19 - Coordinated public release of advisory
- 2018-09-19 - Advisory Updated
