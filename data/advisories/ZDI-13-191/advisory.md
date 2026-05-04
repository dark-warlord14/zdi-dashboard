# ZDI-13-191: Oracle Endeca Server attachDataStore SOAP Request Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-191
- **ZDI-CAN:** ZDI-CAN-1787
- **Date:** 2013-08-13
- **CVE:** CVE-2013-3764
- **CVSS:** 6.4
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** Endeca Server
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-191/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Endeca Server. Authentication is not required to exploit this vulnerability. The specific flaw exists in the handling of requests to the controlSoapBinding web service. This service exposes the attachDataStore method which contains a directory traversal flaw that allows attackers to create files at arbitrary locations with attacker controlled data. This can be leveraged by an attacker gain to remote code execution under the context of the current user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpujuly2013-1899826.html

## Disclosure Timeline

- 2013-02-22 - Vulnerability reported to vendor
- 2013-08-13 - Coordinated public release of advisory
