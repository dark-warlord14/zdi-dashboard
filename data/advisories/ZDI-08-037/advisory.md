# ZDI-08-037: Apple QuickTime Indeo Video Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-037
- **ZDI-CAN:** ZDI-CAN-297
- **Date:** 2008-06-10
- **CVE:** CVE-2008-1584
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-037/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Apple Quicktime Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of Quicktime files that utilize the Indeo video codec. A lack of proper bounds checking within Indeo.qtx can result in a stack based buffer overflow leading to arbitrary code execution under the context of the currently logged in user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2008-02-07 - Vulnerability reported to vendor
- 2008-06-10 - Coordinated public release of advisory
