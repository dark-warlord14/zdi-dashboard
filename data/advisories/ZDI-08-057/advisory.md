# ZDI-08-057: Apple QuickTime IV32 Codec Parsing Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-057
- **ZDI-CAN:** ZDI-CAN-376
- **Date:** 2008-09-09
- **CVE:** CVE-2008-3635
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-057/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of QuickTime files that utilize the Indeo video codec. A lack of proper bounds checking within QuickTimeInternetExtras.qtx can result in a stack based buffer overflow leading to arbitrary code execution under the context of the currently logged in user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT3027

## Disclosure Timeline

- 2008-08-19 - Vulnerability reported to vendor
- 2008-09-09 - Coordinated public release of advisory
