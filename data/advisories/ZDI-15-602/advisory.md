# ZDI-15-602: Adobe Flash MovieClip beginGradientFill Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-602
- **ZDI-CAN:** ZDI-CAN-3370
- **Date:** 2015-12-08
- **CVE:** CVE-2015-8050
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-602/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability is in the implementation of the MovieClip.beginGradientFill method. By performing certain actions an attacker can force a MovieClip-related object in memory to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb15-32.html

## Disclosure Timeline

- 2015-11-02 - Vulnerability reported to vendor
- 2015-12-08 - Coordinated public release of advisory
