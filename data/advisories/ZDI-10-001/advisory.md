# ZDI-10-001: Novell iManager eDirectory Plugin Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-001
- **ZDI-CAN:** ZDI-CAN-439
- **Date:** 2010-01-07
- **CVE:** CVE-2009-4486
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** iManager
- **Credit:** 1c239c43f521145fa8385d64a9c32243
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-001/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Novell iManager. Authentication is not required to exploit this vulnerability. The flaw exists in an application called by the iManager in order to handle importing/exporting of schema information. While importing/exporting from the schema, the sub-application fails to validate the length of its arguments while copying user-supplied data into statically allocated stack buffer. This can result in code execution under the privileges of the application.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/viewContent.do?externalId=7004985&sliceId=1

## Disclosure Timeline

- 2009-03-26 - Vulnerability reported to vendor
- 2010-01-07 - Coordinated public release of advisory
