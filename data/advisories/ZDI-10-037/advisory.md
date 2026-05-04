# ZDI-10-037: Apple QuickTime MJPEG Sample Dimensions Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-037
- **ZDI-CAN:** ZDI-CAN-525
- **Date:** 2010-04-02
- **CVE:** CVE-2010-0517
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Damian Put Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-037/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists during the parsing of compressed mjpeg data from a malformed .mov file. The application will utilize the width and height fields in the file for calculating the size of a heap buffer. When copying into this buffer, the application will use a different field in the file to determine when to stop copying. If the first calculated length is smaller than the one used for decompression, a memory corruption will occur which can result in code execution under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4077

## Disclosure Timeline

- 2009-07-14 - Vulnerability reported to vendor
- 2010-04-02 - Coordinated public release of advisory
