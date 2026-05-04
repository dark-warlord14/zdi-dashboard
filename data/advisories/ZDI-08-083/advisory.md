# ZDI-08-083: Microsoft Animation ActiveX Control Malformed AVI Parsing Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-083
- **ZDI-CAN:** ZDI-CAN-387
- **Date:** 2008-12-09
- **CVE:** CVE-2008-4255
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows XP
- **Credit:** CHkr_D591
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-083/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code through vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists within the Microsoft Animation ActiveX control MSCOMCT2.OCX. When parsing a malformed AVI file through this control an exploitable heap corruption can occur. As the AVI file can be loaded over a UNC path this issue is remotely exploitable and can result in arbitrary code execution under the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS08-070.mspx

## Disclosure Timeline

- 2008-09-16 - Vulnerability reported to vendor
- 2008-12-09 - Coordinated public release of advisory
