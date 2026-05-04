# ZDI-12-079: Apple QuickTime H264 Picture Width Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-079
- **ZDI-CAN:** ZDI-CAN-1460
- **Date:** 2012-06-06
- **CVE:** CVE-2012-0665
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-079/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the QuicktimeH264 modules in the QuickTime player that handles H264 encoded movies. When the value for 'pic_width_in_mbs_minus_1' and 'pic_height_in_map_units_minus_1' in the AVCC header data differs from the actual picture width and height a heap buffer overflow occurs. This can result in remote code execution under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT5261

## Disclosure Timeline

- 2011-11-29 - Vulnerability reported to vendor
- 2012-06-06 - Coordinated public release of advisory
