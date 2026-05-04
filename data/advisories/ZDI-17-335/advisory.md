# ZDI-17-335: Adobe Reader DC PDF Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-335
- **ZDI-CAN:** ZDI-CAN-4550
- **Date:** 2017-05-12
- **CVE:** CVE-2017-3040
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** riusksk of Tencent Security Platform Department
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-335/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Adobe Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within Reader's PDF parsing. The process does not properly validate user-supplied data which can result in a read past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb17-11.html

## Disclosure Timeline

- 2017-03-24 - Vulnerability reported to vendor
- 2017-05-12 - Coordinated public release of advisory
