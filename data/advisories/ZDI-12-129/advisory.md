# ZDI-12-129: Microsoft Windows TrueType Font Parsing Remote Code Execution Vulnerability (Remote Kernel)

## Metadata

- **ZDI ID:** ZDI-12-129
- **ZDI-CAN:** ZDI-CAN-1338
- **Date:** 2012-08-03
- **CVE:** CVE-2012-0159
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft, Microsoft, Microsoft
- **Affected Products:** Windows XP SP3, Windows Vista, Windows 7
- **Credit:** Alin Rad Pop (binaryproof)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-129/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code from the contact of kernelspace on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the kernel's support for TrueType font parsing of compound glyphs. A sign extension error exists in win32k.sys when processing compound glyphs having a total number of contours above 0x7FFF. This can be exploited to corrupt kernel heap memory placed below the space allocated for the "flags" buffer and potentially execute arbitrary code in kernel space.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/ms12-039 Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/ms12-039 Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/ms12-039

## Disclosure Timeline

- 2011-11-04 - Vulnerability reported to vendor
- 2012-08-03 - Coordinated public release of advisory
