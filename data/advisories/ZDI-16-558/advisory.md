# ZDI-16-558: Acrobat Reader DC XFA template Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-558
- **ZDI-CAN:** ZDI-CAN-3925
- **Date:** 2016-10-11
- **CVE:** CVE-2016-6951
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Sebastian Apelt siberas
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-558/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of template objects. The process does not properly validate user-supplied data which can result in a read past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb16-33.html

## Disclosure Timeline

- 2016-07-28 - Vulnerability reported to vendor
- 2016-10-11 - Coordinated public release of advisory
