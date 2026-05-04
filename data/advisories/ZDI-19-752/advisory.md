# ZDI-19-752: Adobe Acrobat Pro DC JPEG File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-752
- **ZDI-CAN:** ZDI-CAN-8694
- **Date:** 2019-08-19
- **CVE:** CVE-2019-8040
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** willJ
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-752/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of JPEG files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb19-41.html

## Disclosure Timeline

- 2019-06-20 - Vulnerability reported to vendor
- 2019-08-19 - Coordinated public release of advisory
