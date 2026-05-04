# ZDI-08-018: Apple QuickTime Run Length Encoding Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-018
- **ZDI-CAN:** ZDI-CAN-296
- **Date:** 2008-04-03
- **CVE:** CVE-2008-1021
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-018/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Apple QuickTime Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of QuickTime files that utilize the Animation codec. A lack of proper length checks can result in a heap based buffer overflow leading to arbitrary code execution under the context of the currently logged in user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1241

## Disclosure Timeline

- 2008-02-07 - Vulnerability reported to vendor
- 2008-04-03 - Coordinated public release of advisory
