# ZDI-12-143: Microsoft Visio DWGDP MTEXT Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-143
- **ZDI-CAN:** ZDI-CAN-1531
- **Date:** 2012-08-17
- **CVE:** CVE-2012-1888
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Office
- **Credit:** Alexander Gavrun
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-143/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Visio. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within DWGDP.DLL, which is responsible for parsing DXF files. When processing MTEXT strings in the ENTITIES section of the DXF file, certain characters are sought after to end the string copy function. If these characters are not found, the copy function will continue to copy data outside of the stack buffer, causing memory corruption. An attacker can utilize this vulnerability to execute code under the context of the program.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/ms12-059

## Disclosure Timeline

- 2012-03-14 - Vulnerability reported to vendor
- 2012-08-17 - Coordinated public release of advisory
