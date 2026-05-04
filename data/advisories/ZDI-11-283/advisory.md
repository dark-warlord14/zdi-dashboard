# ZDI-11-283: Adobe Reader Image Data Buffer Allocation Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-283
- **ZDI-CAN:** ZDI-CAN-1211
- **Date:** 2011-10-13
- **CVE:** CVE-2011-2438
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** binaryproof
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-283/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Adobe Image parsing library. When Adobe Reader tries to parse an malformed .BMP image with bitfields encoded image data an integer overflow can occur while calculation the size of the image data. This can result in a heap buffer overflow with remote code execution under the context of the current user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-24.html

## Disclosure Timeline

- 2011-05-12 - Vulnerability reported to vendor
- 2011-10-13 - Coordinated public release of advisory
