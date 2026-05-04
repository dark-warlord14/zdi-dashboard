# ZDI-17-287: Adobe Flash PSDKEvent Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-287
- **ZDI-CAN:** ZDI-CAN-4565
- **Date:** 2017-04-19
- **CVE:** CVE-2017-2994
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** bo13oy of CloverSec Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-287/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of PSDKEvent objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb17-07.html

## Disclosure Timeline

- 2017-03-09 - Vulnerability reported to vendor
- 2017-04-19 - Coordinated public release of advisory
