# ZDI-15-299: Samsung SyncThru FileUploadController Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-299
- **ZDI-CAN:** ZDI-CAN-2582
- **Date:** 2015-07-13
- **CVE:** CVE-2015-5473
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Samsung
- **Affected Products:** SyncThru
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-299/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Samsung SyncThru. By default, authentication is not required to exploit this vulnerability. The specific flaw exists within the FileUploadController servlet exposed by uploadFirmware.html. The issue lies in the failure to sanitize the path of files uploaded, allowing for them to be placed anywhere on the server. An attacker can leverage this vulnerability to execute arbitrary code as SYSTEM.

## Additional Details

Resolved by: Samsung SyncThu 6 v1.0

## Disclosure Timeline

- 2015-05-27 - Vulnerability reported to vendor
- 2015-07-13 - Coordinated public release of advisory
