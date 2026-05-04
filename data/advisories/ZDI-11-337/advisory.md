# ZDI-11-337: RealNetworks RealPlayer RV30 Uninitialized Index Value Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-337
- **ZDI-CAN:** ZDI-CAN-1303
- **Date:** 2011-11-28
- **CVE:** CVE-2011-4256
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-337/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks Real Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application parses sample data encoded with the RV30 codec. When parsing this sample data, the application will make an allocation and then fail to completely initialize the buffer. During decoding of the sample data, the application will explicitly trust an index from the partially filled buffer and then use that to calculate an address to write to. This can lead to memory corruption which can be converted into code execution under the context of the application.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/11182011_player/en/

## Disclosure Timeline

- 2011-08-12 - Vulnerability reported to vendor
- 2011-11-28 - Coordinated public release of advisory
