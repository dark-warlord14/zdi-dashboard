# ZDI-14-048: Apple QuickTime ftab Atom Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-048
- **ZDI-CAN:** ZDI-CAN-1943
- **Date:** 2014-04-03
- **CVE:** CVE-2014-1246
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-048/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of the ftab atom. By providing an overly large font name, an attacker can overflow a fixed size stack buffer. An attacker could use this vulnerability to execute arbitrary code in the context of the user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2013-09-21 - Vulnerability reported to vendor
- 2014-04-03 - Coordinated public release of advisory
