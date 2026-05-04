# ZDI-14-044: Apple QuickTime nam Atom Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-044
- **ZDI-CAN:** ZDI-CAN-1737
- **Date:** 2014-04-03
- **CVE:** CVE-2014-1243
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** Tom Gallagher (Microsoft) & Paul Bates (Microsoft)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-044/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the nam atom in an mp4 file. Manipulation of this atom can corrupt memory and a remote attacker can exploit this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2013-07-13 - Vulnerability reported to vendor
- 2014-04-03 - Coordinated public release of advisory
