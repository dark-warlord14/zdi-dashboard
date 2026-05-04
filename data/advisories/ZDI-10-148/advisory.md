# ZDI-10-148: Microsoft Cinepak Codec CVDecompress Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-148
- **ZDI-CAN:** ZDI-CAN-720
- **Date:** 2010-08-10
- **CVE:** CVE-2010-2553
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** File Format Vulnerability
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-148/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the iccvid.dll module responsible for compression and decompression of VIDC (Cinepak) streams. The code within CVDecompress allocates a static amount of space for storing an RGB palette. By modifying a VIDC compressed stream within an AVI file, an attacker can force code within iccvid to loop excessively, each time incrementing the pointer for the palette storage. By abusing this behavior an attacker can execute arbitrary code under the context of the user invoking the application that uses this codec.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/Bulletin/MS10-055.mspx

## Disclosure Timeline

- 2010-04-13 - Vulnerability reported to vendor
- 2010-08-10 - Coordinated public release of advisory
