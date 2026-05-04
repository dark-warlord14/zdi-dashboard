# ZDI-10-002: Oracle Secure Backup observiced.exe Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-002
- **ZDI-CAN:** ZDI-CAN-471
- **Date:** 2010-01-12
- **CVE:** CVE-2010-0072
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Secure Backup
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-002/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Secure Backup. Authentication is not required to exploit this vulnerability. The specific flaw exists in the Oracle Secure Backup Services daemon observiced.exe listening on TCP port 10000 by default. Due to the lack of bounds checking on the reverse lookup of connections to the port a stack-based buffer overflow can occur leading to a complete compromise of the affected system under the credentials of the SYSTEM account.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technology/deploy/security/critical-patch-updates/cpujan2010.html

## Disclosure Timeline

- 2009-04-20 - Vulnerability reported to vendor
- 2010-01-12 - Coordinated public release of advisory
