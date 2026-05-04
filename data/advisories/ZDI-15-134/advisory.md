# ZDI-15-134: (Pwn2Own) Adobe Flash Player AS3 ConvolutionFilter Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-134
- **ZDI-CAN:** ZDI-CAN-2819
- **Date:** 2015-04-15
- **CVE:** CVE-2015-0349
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash Player
- **Credit:** Nicolas Joly
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-134/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of AS3 ConvolutionFilter objects. By manipulating the matrix property of a ConvolutionFilter object, an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb15-06.html

## Disclosure Timeline

- 2015-03-18 - Vulnerability reported to vendor
- 2015-04-15 - Coordinated public release of advisory
