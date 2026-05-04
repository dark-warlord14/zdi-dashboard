# ZDI-11-277: Apple QuickTime 3g2 'mp4v' atom size Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-277
- **ZDI-CAN:** ZDI-CAN-1285
- **Date:** 2011-08-31
- **CVE:** CVE-2011-0258
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-277/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Quicktime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Quicktime handles 'mp4v' codec information. When parsing the video description table it will read the size field preceding the 'mp4v' tag and use that size to create an allocation to hold the data. It will then copy the correct amount of data into that buffer, but then does some endian changes on a fixed portion of the buffer without checking its size. The resulting memory corruption could result in remote code execution under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4826

## Disclosure Timeline

- 2011-06-03 - Vulnerability reported to vendor
- 2011-08-31 - Coordinated public release of advisory
