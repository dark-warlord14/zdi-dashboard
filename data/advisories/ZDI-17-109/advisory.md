# ZDI-17-109: Adobe Flash Player MessageChannel Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-109
- **ZDI-CAN:** ZDI-CAN-4371
- **Date:** 2017-02-14
- **CVE:** CVE-2017-2995
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** bo13oy of CloverSec Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-109/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of data passed within MessageChannel objects. The issue results from the lack of proper validation of user-supplied data which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb17-04.html

## Disclosure Timeline

- 2016-12-20 - Vulnerability reported to vendor
- 2017-02-14 - Coordinated public release of advisory
