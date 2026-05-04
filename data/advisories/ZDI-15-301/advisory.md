# ZDI-15-301: Samsung SyncThru AddDriverFileServlet Directory Traversal Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-301
- **ZDI-CAN:** ZDI-CAN-2586
- **Date:** 2015-07-13
- **CVE:** CVE-2015-5473
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:N/A:C
- **Affected Vendors:** Samsung
- **Affected Products:** SyncThru
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-301/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files on vulnerable installations of Samsung SyncThru. By default, authentication is not required to exploit this vulnerability. The specific flaw exists within the AddDriverFileServlet servlet exposed by upload/addDriver. The issue lies in the failure to sanitize the path of files uploaded, allowing for the deletion of any file on the system. An attacker could use this to create a denial-of-service condition.

## Additional Details

Resolved by: Samsung SyncThu 6 v1.0

## Disclosure Timeline

- 2015-05-18 - Vulnerability reported to vendor
- 2015-07-13 - Coordinated public release of advisory
