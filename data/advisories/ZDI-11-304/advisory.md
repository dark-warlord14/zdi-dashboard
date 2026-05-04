# ZDI-11-304: Apple Quicktime Advanced Audio Codec Frame Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-304
- **ZDI-CAN:** ZDI-CAN-1150
- **Date:** 2011-10-26
- **CVE:** CVE-2011-3252
- **CVSS:** 8.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-304/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime Player. Authentication is not required to exploit this vulnerability. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application parses an audio stream encoded with the advanced audio codec. A field will be read from the file in order to calculate a length that is later used in a memory copy operation into a statically sized buffer. Successful exploitation can lead to code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4981

## Disclosure Timeline

- 2011-04-11 - Vulnerability reported to vendor
- 2011-10-26 - Coordinated public release of advisory
