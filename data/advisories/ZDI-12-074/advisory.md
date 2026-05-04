# ZDI-12-074: Oracle Forms Recognition CroScPlt.dll ActiveX Control Remote Code Execution Vulnerabilty

## Metadata

- **ZDI ID:** ZDI-12-074
- **ZDI-CAN:** ZDI-CAN-1399
- **Date:** 2012-04-19
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** WebCenter Forms Recognition
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-074/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle WebCenter Forms Recognition. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the CroScPlt.dll ActiveX Control. The ActiveX control contains a vulnerable Save() method which allows creation or overwriting of files with arbitrary extensions inside arbitrary locations. This vulnerability can be leveraged to execute code under the context of the user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpuapr2012-366314.html

## Disclosure Timeline

- 2011-10-21 - Vulnerability reported to vendor
- 2012-04-19 - Coordinated public release of advisory
