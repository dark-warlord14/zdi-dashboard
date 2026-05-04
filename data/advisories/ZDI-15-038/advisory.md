# ZDI-15-038: (0Day) Persistent Systems Client Automation Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-038
- **ZDI-CAN:** ZDI-CAN-2142
- **Date:** 2015-02-10
- **CVE:** CVE-2015-1497
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Persistent Systems
- **Affected Products:** Radia Client Automation
- **Credit:** Ben Turner
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-038/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Persistent Systems Client Automation. Authentication is not required to exploit this vulnerability. The flaw exists within the radexecd.exe component which listens by default on TCP port 3465. When handling a remote execution request the process does not properly authenticate the user issuing the request. The command to be executed is also not properly sanitized. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of SYSTEM. This vulnerability is different than ZDI-11-105.

## Additional Details

Persistent Systems has issued an update to correct this vulnerability. More details can be found at: https://radiasupport.accelerite.com/hc/en-us/articles/203659814-Accelerite-releases-solutions-and-best-practices-to-enhance-the-security-for-RBAC-and-Remote-Notify-features

## Disclosure Timeline

- 2014-04-16 - Vulnerability reported to vendor
- 2015-02-10 - Coordinated public release of advisory
