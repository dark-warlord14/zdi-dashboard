# ZDI-08-059: Apple QuickTime STSZ Atom Parsing Heap Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-059
- **ZDI-CAN:** ZDI-CAN-328
- **Date:** 2008-09-09
- **CVE:** CVE-2008-3626
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-059/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists in the handling of STSZ atoms within the function CallComponentFunctionWithStorage(). When an entry in the sample_size_table is too large, a memory corruption occurs which can be further leveraged to execute arbitrary code under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT3027

## Disclosure Timeline

- 2008-05-15 - Vulnerability reported to vendor
- 2008-09-09 - Coordinated public release of advisory
