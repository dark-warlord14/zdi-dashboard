# ZDI-08-060: Apple QuickTime AVC1 Atom Parsing Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-060
- **ZDI-CAN:** ZDI-CAN-304
- **Date:** 2008-09-09
- **CVE:** CVE-2008-3627
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-060/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Apple QuickTime Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists in the parsing of AVC1 atoms. An integer overflow condition is present that can result in a heap chunk being under-allocated. This heap corruption can be further leveraged to execute arbitrary code under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT3027

## Disclosure Timeline

- 2008-05-15 - Vulnerability reported to vendor
- 2008-09-09 - Coordinated public release of advisory
