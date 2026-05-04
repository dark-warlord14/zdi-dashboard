# ZDI-10-040: Apple QuickTime RLE Bit Depth Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-040
- **ZDI-CAN:** ZDI-CAN-545
- **Date:** 2010-04-02
- **CVE:** CVE-2010-0516
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-040/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists during the parsing of samples from a malformed .mov file utilizing the RLE codec. While decoding RLE data, the application will fail to validate the size when decompressing the data into a heap chunk. If the length is larger than the size of the chunk allocated, then a memory corruption will occur which can lead to code execution under the context of the currently logged in user.

## Disclosure Timeline

- 2009-08-10 - Vulnerability reported to vendor
- 2010-04-02 - Coordinated public release of advisory
