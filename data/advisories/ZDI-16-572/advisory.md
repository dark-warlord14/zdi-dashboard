# ZDI-16-572: Oracle WebLogic Commons DiskFileItem Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-572
- **ZDI-CAN:** ZDI-CAN-3591
- **Date:** 2016-11-01
- **CVE:** CVE-2016-5535
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** WebLogic
- **Credit:** Jacob Baines - Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-572/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle WebLogic. Authentication is not required to exploit this vulnerability. The specific flaw exists within the use of Apache Commons DiskFileItem. It is possible to execute arbitrary commands upon deserialization of untrusted data. The attacker can leverage this vulnerability to execute code in the context of the process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/security-advisory/cpuoct2016-2881722.html

## Disclosure Timeline

- 2016-04-12 - Vulnerability reported to vendor
- 2016-11-01 - Coordinated public release of advisory
