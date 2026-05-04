# ZDI-18-1428: Adobe Acrobat Pro DC EMF Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1428
- **ZDI-CAN:** ZDI-CAN-6721
- **Date:** 2018-12-19
- **CVE:** CVE-2018-19721
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** GDPR
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1428/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of EMF files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb18-34.html

## Disclosure Timeline

- 2018-09-06 - Vulnerability reported to vendor
- 2018-12-19 - Coordinated public release of advisory
- 2023-06-22 - Advisory Updated
