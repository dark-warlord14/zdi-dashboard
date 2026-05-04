# ZDI-08-020: Microsoft GDI WMF Parsing Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-020
- **ZDI-CAN:** ZDI-CAN-295
- **Date:** 2008-04-08
- **CVE:** CVE-2008-1083
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft, Microsoft, Microsoft, Microsoft
- **Affected Products:** Windows XP SP2 Windows 2003 SP1 Windows Vista Windows 2000 SP4
- **Credit:** Sebastian Apelt (webmaster@buzzworld.org)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-020/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required in that a user must open a malicious file or visit a malicious web page. The specific flaw exists within the parsing of malformed WMF files. A vulnerability exists in the GDI funcion CreateDIBPatternBrushPt used when processing WMF files. Due to a mis-calculation of user data a heap chunk can be under-allocated and later used resulting in a heap overflow. Successful exploitation can result in system compromise under the credentials of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms08-021.mspx

## Disclosure Timeline

- 2008-02-07 - Vulnerability reported to vendor
- 2008-04-08 - Coordinated public release of advisory
