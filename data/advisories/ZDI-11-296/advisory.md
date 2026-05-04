# ZDI-11-296: Adobe Reader BMP Image RLE Decoding Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-296
- **ZDI-CAN:** ZDI-CAN-1212
- **Date:** 2011-10-26
- **CVE:** CVE-2011-2438
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** binaryproof
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-296/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Adobe Image parsing library. When Adobe Reader tries to parse an malformed .BMP image containing Run Length Encoded data it fails to perform sufficient boundary checks on the data. The effect can be a heap buffer overflow resulting in remote code execution under the context of the current user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-24.html

## Disclosure Timeline

- 2011-05-12 - Vulnerability reported to vendor
- 2011-10-26 - Coordinated public release of advisory
