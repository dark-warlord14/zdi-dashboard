# ZDI-16-425: Adobe Flash PrintJob printAsBitmap Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-425
- **ZDI-CAN:** ZDI-CAN-3780
- **Date:** 2016-07-12
- **CVE:** CVE-2016-4222
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** Jaehun Jeong(@n3sk) of WINS WSEC Analysis Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-425/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of PrintJob objects. By setting the printAsBitmap property with a specific value, an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb16-25.html

## Disclosure Timeline

- 2016-05-26 - Vulnerability reported to vendor
- 2016-07-12 - Coordinated public release of advisory
