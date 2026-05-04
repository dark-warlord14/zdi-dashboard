# ZDI-10-289: Microsoft Internet Explorer HTML+Time Element outerText Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-289
- **ZDI-CAN:** ZDI-CAN-725
- **Date:** 2010-12-14
- **CVE:** CVE-2010-3346
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Peter Vreugdenhil ( http://vreugdenhilresearch.nl )
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-289/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must be convinced of visiting a malicious page or opening a malicious file. The specific flaw exists within usage of a particular element that's part of the Timed Interactive Multimedia Extensions component of the browser. By removing an element referenced by a tag used for implementing an animation, the application can be made to access an element that has been previously freed. Successful exploitation can lead to code execution under the context of the application.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS10-090.mspx

## Disclosure Timeline

- 2010-06-17 - Vulnerability reported to vendor
- 2010-12-14 - Coordinated public release of advisory
