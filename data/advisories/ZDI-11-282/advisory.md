# ZDI-11-282: Adobe Reader U3D BMP Colors Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-282
- **ZDI-CAN:** ZDI-CAN-1196
- **Date:** 2011-10-13
- **CVE:** CVE-2011-2438
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** binaryproof
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-282/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Adobe Image parsing library. When Adobe Reader tries to parse an malformed .BMP image it fails to calculate the correct size to hold the color data. This can result in a heap buffer overflow with remote code execution under the context of the current user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-24.html

## Disclosure Timeline

- 2011-05-12 - Vulnerability reported to vendor
- 2011-10-13 - Coordinated public release of advisory
