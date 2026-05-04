# ZDI-12-059: Mozilla Firefox Ogg Vorbis Decoding Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-059
- **ZDI-CAN:** ZDI-CAN-1477
- **Date:** 2012-04-09
- **CVE:** CVE-2012-0444
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-059/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists in the parsing of Ogg Vorbis media files. By crafting a stream with specific values , it is possible to cause a decoding loop that copies memory to write controlled data beyond the end of a fixed size buffer. An attacker can leverage this behavior to gain remote code execution under the context of the current process.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2012/mfsa2012-07.html

## Disclosure Timeline

- 2012-01-12 - Vulnerability reported to vendor
- 2012-04-09 - Coordinated public release of advisory
