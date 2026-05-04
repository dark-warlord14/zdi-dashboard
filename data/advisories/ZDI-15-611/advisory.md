# ZDI-15-611: Adobe Flash AS2 DisplacementMapFilter mapBitmap Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-611
- **ZDI-CAN:** ZDI-CAN-3259
- **Date:** 2015-12-08
- **CVE:** CVE-2015-8448
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** Bilou
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-611/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the DisplacementMapFilter object. By manipulating the mapBitmap property of a DisplacementMapFilter object, an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb15-32.html

## Disclosure Timeline

- 2015-09-01 - Vulnerability reported to vendor
- 2015-12-08 - Coordinated public release of advisory
