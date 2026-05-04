# ZDI-13-199: Oracle Database Server SQL QName Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-199
- **ZDI-CAN:** ZDI-CAN-1560
- **Date:** 2013-08-13
- **CVE:** CVE-2013-3751
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Database Server
- **Credit:** Nicolas Gregoire
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-199/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Database. Authentication is not required to exploit this vulnerability. The specific flaw exists in the LpxFSMDom function. This function is responsible for parsing SQL commands through XML. A specially crafted QName used in a SQL SELECT command can result in a stack overflow. An attacker can leverage this vulnerability to execute code under the context of the process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpujuly2013-1899826.html

## Disclosure Timeline

- 2012-11-21 - Vulnerability reported to vendor
- 2013-08-13 - Coordinated public release of advisory
