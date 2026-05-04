# ZDI-15-648: Adobe Flash MovieClip getBounds Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-648
- **ZDI-CAN:** ZDI-CAN-3372
- **Date:** 2015-12-29
- **CVE:** CVE-2015-8638
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-648/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the MovieClip object. By calling the getBounds method of a MovieClip object, an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb16-01.html

## Disclosure Timeline

- 2015-11-17 - Vulnerability reported to vendor
- 2015-12-29 - Coordinated public release of advisory
