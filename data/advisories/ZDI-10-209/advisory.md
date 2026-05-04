# ZDI-10-209: RealNetworks RealPlayer Malformed IVR Pointer Index Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-209
- **ZDI-CAN:** ZDI-CAN-568
- **Date:** 2010-10-15
- **CVE:** CVE-2010-2998
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-209/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists when parsing a RealMedia .IVR file containing malformed sample data. The application utilizes a index in this data stream for seeking into a list of objects. Due to the lack of constraints on this index, one can seek to an arbitrary object located in memory which will lead to code execution under the context of the currently logged in user.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/10152010_player/en/

## Disclosure Timeline

- 2009-08-20 - Vulnerability reported to vendor
- 2010-10-15 - Coordinated public release of advisory
