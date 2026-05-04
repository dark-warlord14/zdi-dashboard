# ZDI-08-016: Apple QuickTime MP4A Atom Parsing Heap Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-016
- **ZDI-CAN:** ZDI-CAN-285
- **Date:** 2008-04-03
- **CVE:** CVE-2008-1018
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-016/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the parsing of the QuickTime Channel Compositor atom. When the movie file contains a malformed 'chan' atom, a heap corruption occurs resulting in the execution of arbitrary code.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1241

## Disclosure Timeline

- 2008-02-07 - Vulnerability reported to vendor
- 2008-04-03 - Coordinated public release of advisory
