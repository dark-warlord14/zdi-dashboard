# ZDI-15-164: ManageEngine OpManager MultipartRequestServlet fileName Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-164
- **ZDI-CAN:** ZDI-CAN-2440
- **Date:** 2015-04-29
- **CVE:** N/A
- **CVSS:** 6.4
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:P/A:P
- **Affected Vendors:** ManageEngine
- **Affected Products:** OpManager
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-164/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial of service condition on vulnerable installations of ManageEngine OpManager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the multipartRequest servlet. The issue lies in the failure to properly sanitize a filename. A remote attacker can exploit this vulnerability to delete files from the system.

## Additional Details

Upgrade to Build 11500, or higher, to address this vulnerability.

## Disclosure Timeline

- 2014-08-18 - Vulnerability reported to vendor
- 2015-04-29 - Coordinated public release of advisory
