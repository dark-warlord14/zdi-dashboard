# ZDI-10-244: Apple Quicktime Movie Malformed H.264 Sample Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-244
- **ZDI-CAN:** ZDI-CAN-602
- **Date:** 2010-11-09
- **CVE:** CVE-2010-0515
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-244/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists during the parsing of samples from a malformed MOV file utilizing the H.264 codec. While parsing data to render the stream, the application will miscalculate a length that is used to initialize a heap chunk that was allocated in a header. If the length is larger than the size of the chunk allocated, then a memory corruption will occur which can lead to code execution under the context of the application.

## Additional Details

Fixed in QuickTime 7.6.6 http://support.apple.com/kb/HT4104

## Disclosure Timeline

- 2009-12-04 - Vulnerability reported to vendor
- 2010-11-09 - Coordinated public release of advisory
