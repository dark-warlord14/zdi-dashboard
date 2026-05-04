# ZDI-11-340: Apple Quicktime Font Table Signed Length Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-340
- **ZDI-CAN:** ZDI-CAN-1302
- **Date:** 2011-12-07
- **CVE:** CVE-2011-3248
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-340/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Quicktime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application parses font names embedded within an atom. When parsing the font name, the application will treat a length from the file as a signed value when copying font data into a buffer. Due to an unsigned promotion, this can be used to write outside the bounds of a buffer which can lead to code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT5016

## Disclosure Timeline

- 2011-07-20 - Vulnerability reported to vendor
- 2011-12-07 - Coordinated public release of advisory
