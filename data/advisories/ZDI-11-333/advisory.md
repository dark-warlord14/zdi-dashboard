# ZDI-11-333: RealNetworks RealPlayer ATRC Code Data Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-333
- **ZDI-CAN:** ZDI-CAN-1311
- **Date:** 2011-11-28
- **CVE:** CVE-2011-4250
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-333/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the ATRC codec parses sample data out of the media file. When reading bit sizes from the sample, the application will seek a structure that is used for consuming bits from the sample stream outside the bounds of the correct data. When decoding the sample, the application will use the transformed data to initialize another structure. Due to the sizes being unbound, this can be used to corrupt memory outside the original allocation. This type of memory corruption can be leveraged to gain code execution under the context of the application.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/11182011_player/en/

## Disclosure Timeline

- 2011-08-12 - Vulnerability reported to vendor
- 2011-11-28 - Coordinated public release of advisory
