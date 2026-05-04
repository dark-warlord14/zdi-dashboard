# ZDI-16-002: Apple QuickTime ID3 Tag Heap Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-002
- **ZDI-CAN:** ZDI-CAN-3337
- **Date:** 2016-01-08
- **CVE:** CVE-2015-7092
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** Jaanus Kp - Clarified Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-002/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of ID3 version tags in MP3 files. By providing a malformed TXXX frame, an attacker can cause data to be written past the end of an allocated heap buffer. An attacker could leverage this to execute arbitrary code under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT205638

## Disclosure Timeline

- 2015-10-06 - Vulnerability reported to vendor
- 2016-01-08 - Coordinated public release of advisory
