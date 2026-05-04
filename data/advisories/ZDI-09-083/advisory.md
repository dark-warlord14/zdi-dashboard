# ZDI-09-083: Microsoft Excel Shared Feature Header Pointer Offset Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-083
- **ZDI-CAN:** ZDI-CAN-587
- **Date:** 2009-11-10
- **CVE:** CVE-2009-3129
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-083/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Excel. User interaction is required to exploit this vulnerability in that the target must open a malicious spreadsheet. The specific flaw exists in the handling of Shared Feature Header (0x867) tags in an Excel BIFF file format. When processing the cbHdrData size element of the FEATHEADER it is possible to directly control the distance of a calculated pointer. This condition can be leveraged successfully to execute arbitrary code under the context of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS09-067.mspx

## Disclosure Timeline

- 2009-10-20 - Vulnerability reported to vendor
- 2009-11-10 - Coordinated public release of advisory
