# ZDI-11-332: RealNetworks RealPlayer Malformed AAC File Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-332
- **ZDI-CAN:** ZDI-CAN-1310
- **Date:** 2011-11-28
- **CVE:** CVE-2011-4248
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-332/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks Realplayer. AUser interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way RealPLayer handles AAC files. When parsing an AAC file, Realplayer will create buffers based on the type of Channel it finds in the first frame. When the AAC starts with a Single channel in the first frame, and then changes to a channel pair in the following frame, Realplayer fails to update the buffer size for the channel data. The buffer overwrite that follows could result in remote code execution under the context of the current user.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/11182011_player/en/

## Disclosure Timeline

- 2011-07-20 - Vulnerability reported to vendor
- 2011-11-28 - Coordinated public release of advisory
