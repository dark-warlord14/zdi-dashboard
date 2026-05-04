# ZDI-14-049: Apple QuickTime clef Atom Heap Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-049
- **ZDI-CAN:** ZDI-CAN-1945
- **Date:** 2014-04-03
- **CVE:** CVE-2014-1251
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** Aliz Hammond
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-049/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of the clef atom. An attacker can use this flaw to overflow an improperly allocated buffer, which could allow for the execution of arbitrary code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2013-11-03 - Vulnerability reported to vendor
- 2014-04-03 - Coordinated public release of advisory
