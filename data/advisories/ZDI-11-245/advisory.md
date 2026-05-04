# ZDI-11-245: Sybase Adaptive Server Backup and Monitor Server Translation Array Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-245
- **ZDI-CAN:** ZDI-CAN-1077
- **Date:** 2011-07-29
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Sybase
- **Affected Products:** Adaptive Server
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-245/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Sybase Adaptive Server Enterprise. Authentication is not required to exploit this vulnerability. The specific flaw exists within the way Sybase Backup and Monitor servers handle certain data in the login packets. Malformed packets can cause the service in question to lookup a function pointer outside a predefined function pointer array. It is possible to set this function pointer to an address where user controlled data exists and this will result in code execution under the rights of the user running the Monitor Server.

## Additional Details

Sybase has issued an update to correct this vulnerability. More details can be found at: http://www.sybase.com/detail?id=1094235

## Disclosure Timeline

- 2011-01-21 - Vulnerability reported to vendor
- 2011-07-29 - Coordinated public release of advisory
