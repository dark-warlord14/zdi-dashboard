# ZDI-11-229: Apple QuickTime RIFF fmt Chunk Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-229
- **ZDI-CAN:** ZDI-CAN-1124
- **Date:** 2011-06-29
- **CVE:** CVE-2011-0209
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-229/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application parses a specially formatted RIFF WAV file. When parsing a fmt chunk within the file, the application will use a 32-bit field to calculate the size of a buffer to allocate. Before the allocation, the application will add 0x14 bytes to the result. Due to restrictions imposed on the implementation of this component by the language and it's platform, an integer overflow can be made to occur. This can lead to code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4723

## Disclosure Timeline

- 2011-04-11 - Vulnerability reported to vendor
- 2011-06-29 - Coordinated public release of advisory
