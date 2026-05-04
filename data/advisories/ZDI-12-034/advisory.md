# ZDI-12-034: Microsoft Windows Media Player ASX Meta-File Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-034
- **ZDI-CAN:** ZDI-CAN-1400
- **Date:** 2012-02-22
- **CVE:** CVE-2012-0150
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows Media Player
- **Credit:** Alexander Gavrun
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-034/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows Media Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of ASX meta files. When the code within wmp.dll attempts to process the version string within a meta file, it copies it to a fixed-length buffer on the stack without checking that the destination can contain the input data. This can be abused remotely by attackers to execute arbitrary code under the context of the user running the media application.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/MS12-013

## Disclosure Timeline

- 2011-11-04 - Vulnerability reported to vendor
- 2012-02-22 - Coordinated public release of advisory
