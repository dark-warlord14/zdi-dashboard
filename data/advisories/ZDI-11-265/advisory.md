# ZDI-11-265: RealNetworks Realplayer QCP Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-265
- **ZDI-CAN:** ZDI-CAN-1153
- **Date:** 2011-08-16
- **CVE:** CVE-2011-2950
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Sean de Regge
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-265/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within qcpfformat.dll, which is responsible for parsing QCP media files. The process creates a static 256 byte allocation on the heap and trusts a user-supplied counter from the file within a memory copy loop. As the source data is also user-supplied from the file, this can be abused by a remote attacker to execute arbitrary code running in the context of the web browser.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/08162011_player/en/

## Disclosure Timeline

- 2011-04-01 - Vulnerability reported to vendor
- 2011-08-16 - Coordinated public release of advisory
