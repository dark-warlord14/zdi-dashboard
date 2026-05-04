# ZDI-19-876: Adobe Acrobat Pro DC XFA presence Element Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-876
- **ZDI-CAN:** ZDI-CAN-8732
- **Date:** 2019-10-15
- **CVE:** CVE-2019-8064
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** L4Nce
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-876/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of the presence element of an XFA form object. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb19-49.html

## Disclosure Timeline

- 2019-06-25 - Vulnerability reported to vendor
- 2019-10-15 - Coordinated public release of advisory
