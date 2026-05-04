# ZDI-10-201: Oracle Database Java Stored Procedure Race Condition Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-201
- **ZDI-CAN:** ZDI-CAN-667
- **Date:** 2010-10-12
- **CVE:** CVE-2010-2419
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Database Server
- **Credit:** Sami Koivu
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-201/
## Vulnerability Details

This vulnerability allows remote attackers to break out of the Java Sandbox implemented by Oracle's relational database. Authentication is required in that a user must be able to create a Java stored procedure to trigger the issue. The specific flaw exists within Oracle's custom SecurityManager implementation. Due to the implementation's dependence on a flag of a particular object to determine success or failure of a privileged call, a race condition exists which will allow one to execute Java code bypassing the sandbox. Successful exploitation will allow an attacker to execute arbitrary code in the context of the server.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpuoct2010-175626.html

## Disclosure Timeline

- 2010-01-15 - Vulnerability reported to vendor
- 2010-10-12 - Coordinated public release of advisory
