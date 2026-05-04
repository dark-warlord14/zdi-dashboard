# ZDI-12-187: RealNetworks RealPlayer RV20 Frame Size Array Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-187
- **ZDI-CAN:** ZDI-CAN-1350
- **Date:** 2012-11-19
- **CVE:** CVE-2012-0923
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-187/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application parses a particular array contained within a Real Media file and then uses the data. When allocating and reading frame size information, the application will fail to check the bounds of how this array is used. The application will use results in this array as an allocation for the size of a buffer. When initializing this new buffer, the application can then write outside it's bounds which will lead to code execution under the context of the application.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/09072012_player/en/

## Disclosure Timeline

- 2011-10-21 - Vulnerability reported to vendor
- 2012-11-19 - Coordinated public release of advisory
