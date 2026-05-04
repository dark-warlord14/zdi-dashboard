# ZDI-09-090: Microsoft Windows Intel Indeo Codec Parsing Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-090
- **ZDI-CAN:** ZDI-CAN-432
- **Date:** 2009-12-08
- **CVE:** CVE-2009-4310
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft, Microsoft, Microsoft
- **Affected Products:** Windows 2000 SP4, Windows 2003 SP2, Windows XP SP3
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-090/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Microsoft Windows Media Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Intel Indeo41 codec which is accessed by various applications through the Video Compression Manager. This codec is registered to handle IV41 streams within a container such as the AVI format. While decompressing a video stream malicious data can cause a loop to execute excessively and consequently corrupt the application's stack. By providing specific values this can lead to an exploitable condition which can be leveraged by attackers to execute arbitrary code under the context of the user accessing the file.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/advisory/954157.mspx

## Disclosure Timeline

- 2009-03-13 - Vulnerability reported to vendor
- 2009-12-08 - Coordinated public release of advisory
