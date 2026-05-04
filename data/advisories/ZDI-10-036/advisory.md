# ZDI-10-036: Apple QuickTime H.263 PictureHeader Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-036
- **ZDI-CAN:** ZDI-CAN-521
- **Date:** 2010-04-02
- **CVE:** CVE-2010-0062
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Damian Put Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-036/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within quicktime.qts when parsing sample data from a malformed .3g2 file that is utilizing the h.263 codec. While parsing data to render the video stream, the application will miscalculate the length of a buffer. Later when decompressing data to the heap chunk, the application will overflow the under allocated buffer leading to code execution under the context of the currently logged in user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4104

## Disclosure Timeline

- 2009-08-10 - Vulnerability reported to vendor
- 2010-04-02 - Coordinated public release of advisory
