# ZDI-15-278: Apple QuickTime alis Atom Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-278
- **ZDI-CAN:** ZDI-CAN-2700
- **Date:** 2015-07-01
- **CVE:** CVE-2015-3664
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-278/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the alis atom. By providing a malformed alis atom, an attacker is able to cause QuickTime to overflow a stack buffer and execute arbitrary code in the context of the QuickTime process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2015-01-27 - Vulnerability reported to vendor
- 2015-07-01 - Coordinated public release of advisory
