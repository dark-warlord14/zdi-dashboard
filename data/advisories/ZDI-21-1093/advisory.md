# ZDI-21-1093: Adobe Acrobat Pro DC PostScript File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1093
- **ZDI-CAN:** ZDI-CAN-14055
- **Date:** 2021-09-16
- **CVE:** CVE-2021-39858
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** Qiao Li Of Baidu Security Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1093/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PostScript files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb21-55.html

## Disclosure Timeline

- 2021-06-30 - Vulnerability reported to vendor
- 2021-09-16 - Coordinated public release of advisory
