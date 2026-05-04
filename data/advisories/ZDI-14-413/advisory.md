# ZDI-14-413: SAP SQL Anywhere .NET Data Provider SPACE Function Heap Overflow Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-413
- **ZDI-CAN:** ZDI-CAN-2350
- **Date:** 2014-12-09
- **CVE:** CVE-2014-9264
- **CVSS:** 8.5
- **CVSS Vector:** AV:U/AC:M/Au:U/C:P/I:P/A:P
- **Affected Vendors:** SAP
- **Affected Products:** SQL Anywhere
- **Credit:** John Leitch
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-413/
## Vulnerability Details

This allows attackers to execute arbitrary code on applications which pass user provided data to the vulnerable API in SAP SQL Anywhere. The specific flaw exists within the handling of the SPACE function. If an application allows untrusted input to be used as the length of a SPACE function in a query, even if the input is correctly filtered against SQL injection, an attacker could take advantage of an arithmetic truncation error to overflow a heap buffer and execute arbitrary code in the context of the application.

## Additional Details

SAP released Security Note 2057277 ( http://scn.sap.com/docs/DOC-8218 ) to address this issue.

## Disclosure Timeline

- 2014-04-06 - Vulnerability reported to vendor
- 2014-12-09 - Coordinated public release of advisory
