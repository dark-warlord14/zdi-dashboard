# ZDI-11-258: Apple QuickTime STSC atom Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-258
- **ZDI-CAN:** ZDI-CAN-1160
- **Date:** 2011-08-16
- **CVE:** CVE-2011-0249
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Matt "j00ru" Jurczyk
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-258/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Quicktime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Quicktime handles the Sample-to-Chunks table in media files with 'twos' audio codec. If a value for 'samples per chunk' is bigger than 8 times the sample rate from the 'Sample Description Atom' it will cause a buffer overflow during the parsing of the atom sample table. This can result in remote code execution under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4826

## Disclosure Timeline

- 2011-04-11 - Vulnerability reported to vendor
- 2011-08-16 - Coordinated public release of advisory
