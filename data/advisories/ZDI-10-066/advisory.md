# ZDI-10-066: CA XOsoft Control Service entry_point.aspx Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-066
- **ZDI-CAN:** ZDI-CAN-649
- **Date:** 2010-04-06
- **CVE:** CVE-2010-1223
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** CA, CA
- **Affected Products:** XOsoft High Availability, XOsoft Replication
- **Credit:** Andrea Micalizzi aka rgod AbdulAziz Hariri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-066/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Computer Associates XOsoft Control Replication and High Availability Control Service. Authentication is not required to exploit this vulnerability. The specific flaw exists within the /entry_point.aspx service and occurs due to an unbounded string copy utilizing a string controlled by the user as the source into a fixed length buffer located on the stack. Successful exploitation can lead to code execution under the context of the service.

## Additional Details

CA has issued an update to correct this vulnerability. More details can be found at: https://support.ca.com/irj/portal/anonymous/phpsupcontent?contentID=232869

## Disclosure Timeline

- 2009-12-16 - Vulnerability reported to vendor
- 2010-04-06 - Coordinated public release of advisory
