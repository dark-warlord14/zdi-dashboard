# ZDI-17-628: Adobe Acrobat Pro DC XFA PDEContent Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-628
- **ZDI-CAN:** ZDI-CAN-4843
- **Date:** 2017-08-09
- **CVE:** CVE-2017-11256
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** Sebastian Apelt of siberas
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-628/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within XFA's PDEContent object. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb17-24.html

## Disclosure Timeline

- 2017-06-01 - Vulnerability reported to vendor
- 2017-08-09 - Coordinated public release of advisory
