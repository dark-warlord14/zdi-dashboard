# ZDI-15-293: Adobe Flash Player AS2 ConvolutionFilter Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-293
- **ZDI-CAN:** ZDI-CAN-2859
- **Date:** 2015-07-08
- **CVE:** CVE-2015-3039
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** bilou
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-293/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of AS2 ConvolutionFilter objects. By manipulating the matrix property of a ConvolutionFilter object, an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb15-06.html

## Disclosure Timeline

- 2015-04-09 - Vulnerability reported to vendor
- 2015-07-08 - Coordinated public release of advisory
