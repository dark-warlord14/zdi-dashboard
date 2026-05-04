# ZDI-13-248: Oracle Java LDAP Deserialization Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-248
- **ZDI-CAN:** ZDI-CAN-1908
- **Date:** 2013-10-16
- **CVE:** CVE-2013-5830
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Ben Murphy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-248/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of LDAP deserialization. An attacker can use a custom LDAP server to create objects in restricted packages, and leverage this to disable the Java sandbox and execute arbitrary code in the context of the user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpuoct2013-1899837.html

## Disclosure Timeline

- 2013-06-10 - Vulnerability reported to vendor
- 2013-10-16 - Coordinated public release of advisory
