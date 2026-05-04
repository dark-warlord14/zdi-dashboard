# ZDI-11-303: Apple QuickTime H264 Stream frame_cropping Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-303
- **ZDI-CAN:** ZDI-CAN-1314
- **Date:** 2011-10-26
- **CVE:** CVE-2011-3219
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-303/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Quicktime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Quicktime handles H.264 streams. When parsing the Sequence Parameter Set data for a H.264 stream it reads the frame cropping offset fields. When those fields contain incorrect data Quicktime will eventually write outside the buffer allocated for the movie stream. This can result in remote code execution under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4981

## Disclosure Timeline

- 2011-07-20 - Vulnerability reported to vendor
- 2011-10-26 - Coordinated public release of advisory
