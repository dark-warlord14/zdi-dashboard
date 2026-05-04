# ZDI-11-335: RealNetworks RealPlayer RV10 Sample Height Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-335
- **ZDI-CAN:** ZDI-CAN-1305
- **Date:** 2011-11-28
- **CVE:** CVE-2011-4252
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-335/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks Real Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists when the application attempts to parse a height out of the RV10 codec object. The application will incorrectly treat the value as a signed integer and will its value as the count within a loop that populates rows of sample data within a buffer. This can allow for memory corruption which can lead to code execution under the context of the application.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/11182011_player/en/

## Disclosure Timeline

- 2011-08-12 - Vulnerability reported to vendor
- 2011-11-28 - Coordinated public release of advisory
