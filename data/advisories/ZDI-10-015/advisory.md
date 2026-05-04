# ZDI-10-015: Microsoft Windows RLE Video Decompressor Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-015
- **ZDI-CAN:** ZDI-CAN-415
- **Date:** 2010-02-09
- **CVE:** CVE-2010-0250
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft, Microsoft
- **Affected Products:** Windows Vista, Windows XP
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-015/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on applications that utilize DirectShow for rendering video on Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must be coerced into decompressing a malicious video. The specific flaw exists within the decompression of a specific type of video stream contained in an .AVI file. The application misuses a length field for an allocation causing the memory allocation to be too small to contain the subsequent data. During population of this buffer, the application will copy more data than allocated for leading to memory corruption with the potential for code execution.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS10-013.mspx

## Disclosure Timeline

- 2009-01-15 - Vulnerability reported to vendor
- 2010-02-09 - Coordinated public release of advisory
