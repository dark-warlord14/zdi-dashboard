# ZDI-11-050: (0Day) IBM Informix Dynamic Server SET ENVIRONMENT Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-050
- **ZDI-CAN:** ZDI-CAN-405
- **Date:** 2011-02-07
- **CVE:** CVE-2011-1033
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Informix
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-050/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Informix Database Server. SQL query execution privileges are required to exploit this vulnerability. The specific flaw exists within the oninit process bound to TCP port 9088 when processing the arguments to the USELASTCOMMITTED option in a SQL query. User-supplied data is copied into a stack-based buffer without proper bounds checking resulting in an exploitable overflow. Exploitation can result in arbitrary code execution under the context of the database server.

## Additional Details

http://www-01.ibm.com/support/docview.wss?uid=swg1IC74666

## Disclosure Timeline

- 2008-11-10 - Vulnerability reported to vendor
- 2011-02-07 - Coordinated public release of advisory
