# ZDI-09-089: Microsoft Windows Intel Indeo Codec Parsing Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-089
- **ZDI-CAN:** ZDI-CAN-314
- **Date:** 2009-12-08
- **CVE:** CVE-2009-4309
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft, Microsoft, Microsoft
- **Affected Products:** Windows 2000 SP4, Windows 2003 SP2, Windows XP SP3
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-089/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Microsoft Windows Media Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Intel Indeo41 codec which is accessed by various applications through the Video Compression Manager. This codec is registered to handle IV41 streams within a container such as the AVI format. Due to the lack of bounds checking on a specified size within the 'movi' record a heap overflow can occur. If successfully exploited this vulnerability can allow attackers to execute arbitrary code under the context of the user accessing the file.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/advisory/954157.mspx

## Disclosure Timeline

- 2008-04-07 - Vulnerability reported to vendor
- 2009-12-08 - Coordinated public release of advisory
