# ZDI-09-040: Microsoft Office Excel QSIR Record Pointer Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-040
- **ZDI-CAN:** ZDI-CAN-454
- **Date:** 2009-06-10
- **CVE:** CVE-2009-1134
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-040/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Excel. Exploitation requires user interaction in that a victim must open a malicious XLS file. The specific flaw exists within the parsing of the BIFF file format used by Microsoft Excel. When Excel 2007 encounters a malformed Qsir record (0x806) user data is improperly handled leading to potential code execution. Successful exploitation of this can lead to a remote compromise of the affected system running under the credentials of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS09-021.mspx

## Disclosure Timeline

- 2009-03-26 - Vulnerability reported to vendor
- 2009-06-10 - Coordinated public release of advisory
