# ZDI-08-056: Microsoft Windows GDI+ GIF Parsing Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-056
- **ZDI-CAN:** ZDI-CAN-249
- **Date:** 2008-09-09
- **CVE:** CVE-2008-3013
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft, Microsoft, Microsoft, Microsoft
- **Affected Products:** Windows Server 2008, Windows XP, Windows Vista, Windows Server 2003
- **Credit:** Ivan Fratric
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-056/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows XP, Server and Vista. User interaction is required in that a user must open a malicious image file or browse to a malicious website. The specific flaws exist in the GDI+ subsystem when parsing maliciously crafted GIF files. By supplying a malformed graphic control extension an attacker can trigger an exploitable memory corruption condition. Successful exploitation can result in arbitrary code execution under the credentials of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS08-052.mspx

## Disclosure Timeline

- 2008-02-07 - Vulnerability reported to vendor
- 2008-09-09 - Coordinated public release of advisory
