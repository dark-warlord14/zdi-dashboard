# ZDI-16-600: Adobe Flash Player Metadata Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-600
- **ZDI-CAN:** ZDI-CAN-4049
- **Date:** 2016-11-08
- **CVE:** CVE-2016-7861
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** bo13oy of CloverSec Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-600/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Metadata objects. The issue results from the lack of proper validation of user-supplied data which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb16-37.html

## Disclosure Timeline

- 2016-10-06 - Vulnerability reported to vendor
- 2016-11-08 - Coordinated public release of advisory
