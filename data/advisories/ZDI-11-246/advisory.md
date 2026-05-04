# ZDI-11-246: Sybase Adaptive Server Backup and Monitor Server NULL Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-246
- **ZDI-CAN:** ZDI-CAN-1069
- **Date:** 2011-07-29
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Sybase
- **Affected Products:** Adaptive Server
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-246/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Sybase Adaptive Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the way Sybase Backup and Monitor servers handles certain data in the login packets. Malformed packets can cause the service in question to write a NULL byte on the stack which can be leveraged by a remote attacker to execute code under the context of the running service.

## Additional Details

Sybase has issued an update to correct this vulnerability. More details can be found at: http://www.sybase.com/detail?id=1094235

## Disclosure Timeline

- 2011-02-02 - Vulnerability reported to vendor
- 2011-07-29 - Coordinated public release of advisory
