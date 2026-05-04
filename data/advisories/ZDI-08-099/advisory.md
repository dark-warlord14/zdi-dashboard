# ZDI-08-099: Microsoft Office Excel REPT Formula Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-099
- **ZDI-CAN:** ZDI-CAN-357
- **Date:** 2008-10-14
- **CVE:** CVE-2008-4019
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** CHkr_D591
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-099/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office. User interaction is required to exploit this vulnerability in that the target must visit a malicious page, or open a malicious file. The specific flaw exists when parsing Microsoft Excel documents containing a malformed REPT formula embedded inside a cell. During evaluation of this cell Excel miscalculates the size of a static buffer and copies the result of the formula into it resulting in an exploitable condition. This can result in a remote compromise of the system under the credentials of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS08-057.mspx

## Disclosure Timeline

- 2008-06-25 - Vulnerability reported to vendor
- 2008-10-14 - Coordinated public release of advisory
