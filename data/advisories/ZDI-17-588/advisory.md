# ZDI-17-588: Adobe Reader DC XFA closeDoc Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-588
- **ZDI-CAN:** ZDI-CAN-4716
- **Date:** 2017-08-08
- **CVE:** CVE-2017-11223
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-588/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the closeDoc method within an XFA. The process does not properly validate the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb17-24.html

## Disclosure Timeline

- 2017-04-10 - Vulnerability reported to vendor
- 2017-08-08 - Coordinated public release of advisory
