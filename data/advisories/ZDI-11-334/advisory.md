# ZDI-11-334: RealNetworks RealPlayer genr Sample Size Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-334
- **ZDI-CAN:** ZDI-CAN-1279
- **Date:** 2011-11-28
- **CVE:** CVE-2011-4251
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-334/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application processes the audio specific data within a RealMedia audio file. When decoding sample data, the application will explicitly trust a length read from the sample data when populating a buffer that is allocated based on the codec information. Due to this, a memory corruption can be made to occur which can result in code execution within the context of the application.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/11182011_player/en/

## Disclosure Timeline

- 2011-08-12 - Vulnerability reported to vendor
- 2011-11-28 - Coordinated public release of advisory
