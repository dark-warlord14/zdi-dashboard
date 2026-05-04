# ZDI-16-621: Adobe Flash Player BitmapData Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-621
- **ZDI-CAN:** ZDI-CAN-4124
- **Date:** 2016-12-13
- **CVE:** CVE-2016-7875
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** bo13oy of CloverSec Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-621/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of BitmapData objects. The issue results from the lack of proper validation of user-supplied data which can result in a read past the end of an allocated object. An attacker can leverage this vulnerability to execute code under the context of current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb16-39.html

## Disclosure Timeline

- 2016-10-20 - Vulnerability reported to vendor
- 2016-12-13 - Coordinated public release of advisory
