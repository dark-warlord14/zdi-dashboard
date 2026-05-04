# ZDI-14-045: Apple QuickTime stsz Atom Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-045
- **ZDI-CAN:** ZDI-CAN-1860
- **Date:** 2014-04-03
- **CVE:** CVE-2014-1244
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime 7.3
- **Credit:** Tom Gallagher & Paul Bates
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-045/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the stsz atom. By creating a deliberately malformed stsz atom, an attacker is able to cause a heap overflow within the QuickTime parser. Using this vulnerability, an attacker can execute arbitrary code in the context of the user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2013-07-13 - Vulnerability reported to vendor
- 2014-04-03 - Coordinated public release of advisory
