# ZDI-10-103: Microsoft Office Excel DBQueryExt Record Unspecified ADO Object Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-103
- **ZDI-CAN:** ZDI-CAN-666
- **Date:** 2010-06-08
- **CVE:** CVE-2010-1253
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-103/
## Vulnerability Details

This particular vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Excel. User interaction is required in that a target must visit a malicious page or open a malicious file. The specific flaw exists in the parsing of DBQueryExt records in an Excel spreadsheet. Due to the lack of checking when parsing particular fields within the structure, it is possible to get a user-controlled pointer to be called. Successful exploitation can lead to remote code execution under the credentials of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms10-038.mspx

## Disclosure Timeline

- 2010-01-06 - Vulnerability reported to vendor
- 2010-06-08 - Coordinated public release of advisory
