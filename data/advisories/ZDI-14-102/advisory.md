# ZDI-14-102: Oracle Java JPEG Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-102
- **ZDI-CAN:** ZDI-CAN-2038
- **Date:** 2014-04-21
- **CVE:** CVE-2014-2421
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Vitaliy Toropov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-102/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of JPEG images. The issue lies in the ability to control the count parameter to a call to memmove. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpuapr2014-1972952.html

## Disclosure Timeline

- 2013-12-09 - Vulnerability reported to vendor
- 2014-04-21 - Coordinated public release of advisory
