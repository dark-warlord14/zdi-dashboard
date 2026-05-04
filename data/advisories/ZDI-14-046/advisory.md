# ZDI-14-046: Apple QuickTime dref Atom Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-046
- **ZDI-CAN:** ZDI-CAN-1940
- **Date:** 2014-04-03
- **CVE:** CVE-2014-1247
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** Tom Gallagher & Paul Bates
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-046/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the dref atom. It is possible for an attacker to nest atoms within the dref atom that have sizes larger than the enclosing atom. By leveraging this vulnerability, an attacker can execute arbitrary code in the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2013-09-21 - Vulnerability reported to vendor
- 2014-04-03 - Coordinated public release of advisory
