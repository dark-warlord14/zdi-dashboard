# ZDI-11-316: Apple QuickTime H264 Matrix Conversion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-316
- **ZDI-CAN:** ZDI-CAN-1315
- **Date:** 2011-10-27
- **CVE:** CVE-2011-3251
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-316/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Quicktime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Quicktime processes the matrix structures in the 'tkhd' atom for mp4 files. When the matrix structure contains large values a movs instruction can turn the value negative. When Quicktime later uses the function to determine where it should write its data it does check the upper boundaries, but not the lower ones causing a heap buffer underwrite. This can result in remote code execution under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT5016

## Disclosure Timeline

- 2011-07-20 - Vulnerability reported to vendor
- 2011-10-27 - Coordinated public release of advisory
