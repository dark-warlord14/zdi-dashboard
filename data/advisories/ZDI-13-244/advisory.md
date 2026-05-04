# ZDI-13-244: Oracle Java LdapCtx Sandbox Bypass Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-244
- **ZDI-CAN:** ZDI-CAN-1849
- **Date:** 2013-10-16
- **CVE:** CVE-2013-5817
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Ben Murphy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-244/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the com.sun.jndi.ldap.LdapCtx class. The issue lies in the ability to call the toString method of an object in a thread with no user stack. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpuoct2013-1899837.html

## Disclosure Timeline

- 2013-04-16 - Vulnerability reported to vendor
- 2013-10-16 - Coordinated public release of advisory
