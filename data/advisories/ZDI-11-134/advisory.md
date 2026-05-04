# ZDI-11-134: CA Total Defense Suite UNC Management Console RegenerateReport SQL Injection Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-134
- **ZDI-CAN:** ZDI-CAN-1044
- **Date:** 2011-04-13
- **CVE:** CVE-2011-1653
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** CA
- **Affected Products:** Total Defense Suite
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-134/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of CA Total Defense Suite r12. Authentication is not required to exploit this vulnerability. The specific flaw exists within the RegenerateReport stored procedure, accessed via the management.asmx console. The Management Web Service listens for SOAP 1.2 requests on port 34444 for HTTP and 34443 for HTTPS. Due to a flaw in the implementation of the RegenerateReport stored procedure, it is possible for a remote, unauthenticated user to inject arbitrary SQL commands in the SOAP request which could ultimately lead to arbitrary code execution under the context of the SYSTEM user by invoking an exec function.

## Additional Details

CA has issued an update to correct this vulnerability. More details can be found at: https://support.ca.com/irj/portal/anonymous/phpsupcontent?contentID={CD065CEC-AFE2-4D9D-8E0B-BE7F6E345866}

## Disclosure Timeline

- 2011-01-21 - Vulnerability reported to vendor
- 2011-04-13 - Coordinated public release of advisory
