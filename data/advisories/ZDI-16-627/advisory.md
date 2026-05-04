# ZDI-16-627: Adobe Flash Player Worker Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-627
- **ZDI-CAN:** ZDI-CAN-4046
- **Date:** 2016-12-13
- **CVE:** CVE-2016-7871
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** bo13oy of CloverSec Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-627/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Worker objects. The issue results from the lack of proper validation of user-supplied data which can result in a read past the end of an allocated object. An attacker can leverage this vulnerability to execute code under the context of current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb16-39.html

## Disclosure Timeline

- 2016-09-27 - Vulnerability reported to vendor
- 2016-12-13 - Coordinated public release of advisory
