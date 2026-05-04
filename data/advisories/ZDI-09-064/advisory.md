# ZDI-09-064: Apple QuickTime FlashPix Sector Size Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-064
- **ZDI-CAN:** ZDI-CAN-524
- **Date:** 2009-09-10
- **CVE:** CVE-2009-2798
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-064/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists during the parsing of malformed FlashPix (.fpx) files. While parsing the SectorShift and cSectFat fields from the header, the application will multiply 2 user-controlled 32-bit values and utilize this for an allocation. If the result of the multiplication is greater than 32bits, the application will allocate an undersized heap chunk. Later, the application will copy file data directly into this buffer leading to a buffer overflow which can allow for code execution under the context of the currently logged in user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT3859

## Disclosure Timeline

- 2009-07-28 - Vulnerability reported to vendor
- 2009-09-10 - Coordinated public release of advisory
