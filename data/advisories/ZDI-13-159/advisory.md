# ZDI-13-159: Oracle Java ManagedObjectManagerFactory Security Manager Bypass Remote Code Execution Vulnerabillity

## Metadata

- **ZDI ID:** ZDI-13-159
- **ZDI-CAN:** ZDI-CAN-1729
- **Date:** 2013-06-27
- **CVE:** CVE-2013-2455
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Ben Murphy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-159/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the com.sun.org.glassfish.gmbal.ManagedObjectManagerFactor class. The issue lies in the failure to validate permission to access a method during method call. This allows access to methods in classes that would otherwise not be reachable. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpujun2013-1899847.html

## Disclosure Timeline

- 2013-02-22 - Vulnerability reported to vendor
- 2013-06-27 - Coordinated public release of advisory
