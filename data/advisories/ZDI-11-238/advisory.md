# ZDI-11-238: Oracle Secure Backup validate_login Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-238
- **ZDI-CAN:** ZDI-CAN-1165
- **Date:** 2011-07-21
- **CVE:** CVE-2011-2261
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Secure Backup
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-238/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Secure Backup. Authentication is not required to exploit this vulnerability. The specific flaw exists within the validate_login function defined within /apache/htdocts/php/common.php. The username parameter is passed with limited sanitization to an exec_qr call which can be abused to inject commands. The sanitation that does occur can limit the exploitation of this issue, however code execution can likely still be achieved. Successful attempts will yield remote code execution under the context of the apache server.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpujuly2011-313328.html

## Disclosure Timeline

- 2011-04-01 - Vulnerability reported to vendor
- 2011-07-21 - Coordinated public release of advisory
