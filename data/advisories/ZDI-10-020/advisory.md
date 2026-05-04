# ZDI-10-020: EMC HomeBase SSL Service Arbitrary File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-020
- **ZDI-CAN:** ZDI-CAN-644
- **Date:** 2010-02-23
- **CVE:** CVE-2010-0620
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** EMC
- **Affected Products:** HomeBase Server
- **Credit:** Stephen Fewer of Harmony Security (www.harmonysecurity.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-020/
## Vulnerability Details

This vulnerability allows remote attackers to upload arbitrary files on vulnerable installations of EMC HomeBase Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the HomeBase SSL Service due to a failure to sanitize '../' directory traversal modifiers from a parameter. This will allow a user to specify any filename to upload arbitrary contents into. Successful exploitation can result in code execution under the context of the service.

## Additional Details

EMC has released a Security Advisory (ESA-2010-003) identifier to customers through Powerlink.

## Disclosure Timeline

- 2009-12-10 - Vulnerability reported to vendor
- 2010-02-23 - Coordinated public release of advisory
