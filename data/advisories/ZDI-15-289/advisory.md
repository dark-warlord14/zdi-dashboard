# ZDI-15-289: Apple QuickTime code Atom Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-289
- **ZDI-CAN:** ZDI-CAN-2934
- **Date:** 2015-07-01
- **CVE:** CVE-2015-3666
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-289/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the code atom within the Media Information (minf) atom. By malforming this atom, an attacker can cause memory to be accessed after it has been freed. An attacker could leverage this to execute arbitrary code under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT201222

## Disclosure Timeline

- 2015-05-14 - Vulnerability reported to vendor
- 2015-07-01 - Coordinated public release of advisory
