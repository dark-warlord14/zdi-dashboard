# ZDI-08-049: Microsoft Windows Graphics Rendering Engine PICT Heap Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-049
- **ZDI-CAN:** ZDI-CAN-103
- **Date:** 2008-08-12
- **CVE:** CVE-2008-3021
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** File Format Vulnerability
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-049/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Microsoft Office. User interaction is required to exploit this vulnerability in that the target must open a malicious file. The specific flaw exists in the handling of PICT images in an office document. Due to improper parsing of the bits_per_pixel field in a PICT image a heap overflow can occur. Successful exploitation of this vulnerability can lead to a system compromise running under the credentials of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS08-044.mspx

## Disclosure Timeline

- 2006-09-14 - Vulnerability reported to vendor
- 2008-08-12 - Coordinated public release of advisory
