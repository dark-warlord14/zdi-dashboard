# ZDI-18-1370: Adobe Acrobat Pro DC Onix FileClassT Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1370
- **ZDI-CAN:** ZDI-CAN-6900
- **Date:** 2018-12-12
- **CVE:** CVE-2018-16046
- **CVSS:** 5.2
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:C/C:L/I:L/A:L
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** Sebastian Apelt (@bitshifter123)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1370/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of FileClassT objects. By manipulating a document's elements an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb18-41.html

## Disclosure Timeline

- 2018-07-22 - Vulnerability reported to vendor
- 2018-12-12 - Coordinated public release of advisory
