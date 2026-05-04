# ZDI-11-338: RealNetworks RealPlayer IVR MLTI Chunk Length Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-338
- **ZDI-CAN:** ZDI-CAN-1277
- **Date:** 2011-11-28
- **CVE:** CVE-2011-4258
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Damian Put Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-338/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks Real Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application parses a header defined within a .ivr file. When parsing this header the application will explicitly trust a 16-bit value denoting an size and use it for performing an allocation. The code then uses a different value in the file to populate the buffer. Due to the difference in values used for allocation and the copy, this can be used to overwrite data outside the bounds of the buffer which can lead to code execution under the context of the application.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/11182011_player/en/

## Disclosure Timeline

- 2011-08-12 - Vulnerability reported to vendor
- 2011-11-28 - Coordinated public release of advisory
