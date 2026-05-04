# ZDI-09-072: Microsoft Windows GDI+ TIFF Parsing Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-072
- **ZDI-CAN:** ZDI-CAN-605
- **Date:** 2009-10-13
- **CVE:** CVE-2009-2503
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft, Microsoft, Microsoft, Microsoft
- **Affected Products:** Windows Vista, Windows XP, Windows Server 2003, Windows Server 2008
- **Credit:** Ivan Fratric
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-072/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required in that a user must open a malicious image file or browse to a malicious website. The specific flaws exist in the GDI+ subsystem when parsing maliciously crafted TIFF files. By supplying a malformed graphic control extension an attacker can trigger an exploitable memory corruption condition. Successful exploitation can result in arbitrary code execution under the credentials of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms09-062.mspx

## Disclosure Timeline

- 2008-02-07 - Vulnerability reported to vendor
- 2009-10-13 - Coordinated public release of advisory
