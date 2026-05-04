# ZDI-12-043: LibTIFF TileSize Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-043
- **ZDI-CAN:** ZDI-CAN-1221
- **Date:** 2012-03-13
- **CVE:** CVE-2012-1173
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Libtiff
- **Affected Products:** libtiff
- **Credit:** Alexander Gavrun
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-043/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of LibTIFF. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the LibTIFF Library and occurs when the application attempts to allocate space for a tile. When calculating the size for a buffer, the library will perform a multiply which can cause an integer overflow. After allocation, the library will initialize the buffer with tile data. This can cause code execution under the context of the application that utilizes the LibTIFF library.

## Disclosure Timeline

- 2011-05-12 - Vulnerability reported to vendor
- 2012-03-13 - Coordinated public release of advisory
