# ZDI-15-300: Samsung SyncThru DriverFileUploadServlet Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-300
- **ZDI-CAN:** ZDI-CAN-2585
- **Date:** 2015-07-13
- **CVE:** CVE-2015-5473
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Samsung
- **Affected Products:** SyncThru
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-300/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Samsung SyncThru. By default, authentication is not required to exploit this vulnerability. The specific flaw exists within the DriverFileUploadServlet servlet exposed by upload/driver. The issue lies in the failure to sanitize the path of files uploaded, allowing for certain ZIP files to be placed anywhere on the server. An attacker can leverage this vulnerability to execute arbitrary code in the context of the current user.

## Additional Details

Resolved by: Samsung SyncThu 6 v1.0

## Disclosure Timeline

- 2015-05-18 - Vulnerability reported to vendor
- 2015-07-13 - Coordinated public release of advisory
