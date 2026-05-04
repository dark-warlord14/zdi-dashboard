# ZDI-13-116: Apple QuickTime stsd Atom Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-116
- **ZDI-CAN:** ZDI-CAN-1813
- **Date:** 2013-06-11
- **CVE:** CVE-2013-1021
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** Mil3s beep
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-116/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the stsd atom. A malformed stsd atom can be used to cause heap corruption. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2013-03-29 - Vulnerability reported to vendor
- 2013-06-11 - Coordinated public release of advisory
