# ZDI-14-013: Oracle Java TTF Font Parsing Heap Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-013
- **ZDI-CAN:** ZDI-CAN-1979
- **Date:** 2014-02-05
- **CVE:** CVE-2013-5907
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** John Leitch
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-013/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java Runtime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing routines of a ttf font file with a large offset value for a script table. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpujan2014-1972949.html

## Disclosure Timeline

- 2013-09-16 - Vulnerability reported to vendor
- 2014-02-05 - Coordinated public release of advisory
