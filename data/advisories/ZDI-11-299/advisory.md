# ZDI-11-299: Adobe Reader PICT Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-299
- **ZDI-CAN:** ZDI-CAN-1200
- **Date:** 2011-10-26
- **CVE:** CVE-2011-2435
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** binaryproof
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-299/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Adobe 2D.x3d PICT image parsing routines. When Adobe Reader parses an PICT image it uses a static buffer to store certain image header values. Due to insufficient checks for the end of the buffer it is possible to write outside the stack buffer. The resulting stack overflow could result in remote code execution under the context of the current user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-24.html

## Disclosure Timeline

- 2011-05-12 - Vulnerability reported to vendor
- 2011-10-26 - Coordinated public release of advisory
