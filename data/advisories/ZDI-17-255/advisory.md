# ZDI-17-255: Adobe Reader DC JPEG2000 Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-255
- **ZDI-CAN:** ZDI-CAN-4335
- **Date:** 2017-04-11
- **CVE:** CVE-2017-3029
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Giwan Go of STEALIEN
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-255/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Adobe Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within JPEG2000 parsing. The issue results from the lack of proper validation of user-supplied data which can result in a read past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb17-11.html

## Disclosure Timeline

- 2017-01-03 - Vulnerability reported to vendor
- 2017-04-11 - Coordinated public release of advisory
