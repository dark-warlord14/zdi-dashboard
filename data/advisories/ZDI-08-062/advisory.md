# ZDI-08-062: Apple QuickTime MDAT Frame Parsing Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-062
- **ZDI-CAN:** ZDI-CAN-339
- **Date:** 2008-09-09
- **CVE:** CVE-2008-3627
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Subreption LLC
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-062/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists in the parsing of mov video files in QuickTimeH264.scalar. A maliciously crafted MDAT atom can cause a heap corruption resulting in the execution of arbitrary code under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT3027

## Disclosure Timeline

- 2008-05-19 - Vulnerability reported to vendor
- 2008-09-09 - Coordinated public release of advisory
