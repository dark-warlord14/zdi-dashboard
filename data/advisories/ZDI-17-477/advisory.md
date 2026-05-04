# ZDI-17-477: Adobe Flash Player BitmapData applyFilter Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-477
- **ZDI-CAN:** ZDI-CAN-4895
- **Date:** 2017-07-11
- **CVE:** CVE-2017-3100
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** bo13oy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-477/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of BitmapData objects. The issue results from the lack of proper validation of user-supplied data which can result in a read past the end of an allocated object. An attacker can leverage this vulnerability to execute code under the context of current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb17-21.html

## Disclosure Timeline

- 2017-06-08 - Vulnerability reported to vendor
- 2017-07-11 - Coordinated public release of advisory
