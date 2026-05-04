# ZDI-10-274: RealNetworks Realplayer RV20 Stream Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-274
- **ZDI-CAN:** ZDI-CAN-646
- **Date:** 2010-12-10
- **CVE:** CVE-2010-4378
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-274/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists within the module responsible for decompressing RV20 video streams. The drv2.dll trusts a value from the file as a length and uses it within a copy loop that writes to heap memory. By specifying large enough values, heap memory can be corrupted which can lead to arbitrary code execution under the context of the user accessing the media file.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/12102010_player/en/

## Disclosure Timeline

- 2010-01-06 - Vulnerability reported to vendor
- 2010-12-10 - Coordinated public release of advisory
