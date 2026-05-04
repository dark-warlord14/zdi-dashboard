# ZDI-13-095: F-Secure E-mail and Server Security FSDBCom ActiveX Control GetCommand Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-095
- **ZDI-CAN:** ZDI-CAN-1692
- **Date:** 2013-05-29
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** F-Secure
- **Affected Products:** E-mail and Server Security
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-095/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of F-Secure E-mail and Server Security. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the FSDBCom ActiveX control. The issue lies in the failure to sanitize input before executing SQL queries. By carefully constructing a series of SQL queries an attacker can force the backend database to execute arbitrary code. An attacker can leverage this vulnerability to execute code under the context of the backend database.

## Additional Details

http://www.f-secure.com/en/web/labs_global/fsc-2013-1

## Disclosure Timeline

- 2013-02-14 - Vulnerability reported to vendor
- 2013-05-29 - Coordinated public release of advisory
