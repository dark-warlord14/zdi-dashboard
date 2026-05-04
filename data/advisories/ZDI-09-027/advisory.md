# ZDI-09-027: Apple Quicktime PICT Opcode 0x8201 Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-027
- **ZDI-CAN:** ZDI-CAN-412
- **Date:** 2009-06-02
- **CVE:** CVE-2009-0953
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Sebastian Apelt (sebastian.apelt@siberas.de)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-027/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists in the parsing of PICT files in QuickTime.qts. While processing data for opcode 0x8201 QuickTime trusts a value contained in the file and makes an allocation accordingly. The process then enters a loop whose terminating condition is controlled. The previously allocated heap buffer can be overflowed leading to arbitrary code execution under the context of the user running QuickTime.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT3591

## Disclosure Timeline

- 2008-12-17 - Vulnerability reported to vendor
- 2009-06-02 - Coordinated public release of advisory
