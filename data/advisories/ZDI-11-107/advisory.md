# ZDI-11-107: Libtiff ThunderCode Decoder THUNDER_2BITDELTAS Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-107
- **ZDI-CAN:** ZDI-CAN-1004
- **Date:** 2011-03-21
- **CVE:** CVE-2011-1167
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Libtiff
- **Affected Products:** libtiff
- **Credit:** Martin Barbella
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-107/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of libtiff. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the ThunderDecode codec. While decoding a particular code within a row, the decoder will fail to accommodate for the total expanded size of the row. This can cause a heap-based buffer overflow which can lead to code execution under the context of the application utilizing the library.

## Additional Details

Libtiff has issued an update to correct this vulnerability. More details can be found at: http://bugzilla.maptools.org/show_bug.cgi?id=2300

## Disclosure Timeline

- 2011-01-21 - Vulnerability reported to vendor
- 2011-03-21 - Coordinated public release of advisory
