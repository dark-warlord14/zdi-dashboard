# ZDI-10-025: Microsoft Office Excel XLSX File Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-025
- **ZDI-CAN:** ZDI-CAN-499
- **Date:** 2010-03-09
- **CVE:** CVE-2010-0263
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** Anonymous Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-025/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Excel. User interaction is required to exploit this vulnerability in that the target must open a malicious file. The specific flaw exists in the decompression of XLSX files. The XLSX file is a ZIP archive of the associated content making up the new Open XML Document. Due to the lack of validation on the ZIP header when decompressing certain XML elements it is possible to execute uninitialized memory. Successful exploitation can lead to remote code execution under the credentials of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/Bulletin/MS10-017.mspx

## Disclosure Timeline

- 2009-07-14 - Vulnerability reported to vendor
- 2010-03-09 - Coordinated public release of advisory
