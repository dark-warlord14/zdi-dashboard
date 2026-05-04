# ZDI-12-073: Oracle WebCenter Forms Recognition Sssplt30.ocx ActiveX Control Remote Code Execution Vulnerabilty

## Metadata

- **ZDI ID:** ZDI-12-073
- **ZDI-CAN:** ZDI-CAN-1356
- **Date:** 2012-04-19
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** WebCenter Forms Recognition
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-073/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle WebCenter Forms Recognition. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Oracle WebCenter Forms Recognition Sssplt30.ocx ActiveX Control SaveLayout() method. This method allows the creation of replacement of local files with some user controlled data. This can be used to execute remote code under the context of the current user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpuapr2012-366314.html

## Disclosure Timeline

- 2011-11-21 - Vulnerability reported to vendor
- 2012-04-19 - Coordinated public release of advisory
