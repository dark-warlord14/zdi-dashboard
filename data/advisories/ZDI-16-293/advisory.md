# ZDI-16-293: Adobe Reader DC XFAFormInstanceManager Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-293
- **ZDI-CAN:** ZDI-CAN-3451
- **Date:** 2016-05-10
- **CVE:** CVE-2016-1045
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-293/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of XFAFormInstanceManager objects. A specially crafted PDF with an XFA form can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb16-14.html

## Disclosure Timeline

- 2015-12-15 - Vulnerability reported to vendor
- 2016-05-10 - Coordinated public release of advisory
