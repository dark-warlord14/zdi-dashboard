# ZDI-08-055: Microsoft Windows GDI+ BMP Parsing Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-055
- **ZDI-CAN:** ZDI-CAN-211
- **Date:** 2008-09-09
- **CVE:** CVE-2008-3015
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft, Microsoft, Microsoft, Microsoft
- **Affected Products:** Windows XP, Windows Server 2008, Windows Vista, Windows Server 2003
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-055/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows XP, Server and Vista. User interaction is required in that a user must open a malicious image file. The specific flaws exist in the GDI+ subsystem when parsing maliciously crafted BMP files. Supplying a malformed BitMapInfoHeader can result in incorrect integer calculations further leading to an exploitable memory corruption. Successful exploitation can result in arbitrary code execution under the credentials of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS08-052.mspx

## Disclosure Timeline

- 2007-07-20 - Vulnerability reported to vendor
- 2008-09-09 - Coordinated public release of advisory
