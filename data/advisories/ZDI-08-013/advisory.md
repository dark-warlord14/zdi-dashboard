# ZDI-08-013: Novell eDirectory for Linux LDAP delRequest Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-013
- **ZDI-CAN:** ZDI-CAN-214
- **Date:** 2008-03-26
- **CVE:** CVE-2008-0924
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Novell
- **Affected Products:** eDirectory
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-013/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell eDirectory for Linux. Authentication is not required to exploit this vulnerability. The specific flaw exists in the libnldap library. When a large LDAP delRequest message is sent, a stack overflow occurs overwriting a function pointer. This results in a situation allowing the execution of arbitrary code.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/search.do?cmd=displayKC&docType=kc&externalId=3382120&sliceId=SAL_Public&dialogID=59352034&stateId=0%200%2059350122

## Disclosure Timeline

- 2007-07-20 - Vulnerability reported to vendor
- 2008-03-26 - Coordinated public release of advisory
