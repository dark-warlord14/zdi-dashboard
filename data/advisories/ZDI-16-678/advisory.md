# ZDI-16-678: Adobe Flash Player PSDKEventDispatcher Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-678
- **ZDI-CAN:** ZDI-CAN-4332
- **Date:** 2017-02-13
- **CVE:** CVE-2016-7878
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** bee13oy of CloverSec Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-678/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of PSDKEventDispatcher objects. By performing actions in ActionScript an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb16-39.html

## Disclosure Timeline

- 2016-12-12 - Vulnerability reported to vendor
- 2017-02-13 - Coordinated public release of advisory
