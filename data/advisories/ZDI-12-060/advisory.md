# ZDI-12-060: Oracle Java Runtime readMabCurveData nTblSize Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-060
- **ZDI-CAN:** ZDI-CAN-1496
- **Date:** 2012-04-09
- **CVE:** CVE-2012-0498
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-060/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within cmm.dll. While parsing multi-function a to b curve data the size of an allocation is calculated based on user supplied data. It is possible to cause an integer wrap on the nTblSize variable. This variable is later used to allocate an heap buffer which will be smaller than necessary resulting in heap memory corruption. This can lead to remote code execution under the context of the current user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpufeb2012-366318.html

## Disclosure Timeline

- 2012-03-14 - Vulnerability reported to vendor
- 2012-04-09 - Coordinated public release of advisory
