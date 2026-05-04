# ZDI-20-1357: Adobe Acrobat Reader DC AVDocumentLocal Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1357
- **ZDI-CAN:** ZDI-CAN-12015
- **Date:** 2020-11-10
- **CVE:** CVE-2020-24438
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Mark Vincent Yason (@MarkYason)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1357/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the AVDocumentLocal object. By performing actions in JavaScript, an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb20-67.html

## Disclosure Timeline

- 2020-10-02 - Vulnerability reported to vendor
- 2020-11-10 - Coordinated public release of advisory
