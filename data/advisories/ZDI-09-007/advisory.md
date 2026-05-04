# ZDI-09-007: Apple QuickTime Cinepak Codec MDAT Heap Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-007
- **ZDI-CAN:** ZDI-CAN-344
- **Date:** 2009-01-21
- **CVE:** CVE-2009-0006
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-007/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must open a malicious file. The specific flaw exists in the handling of movie data encoded using the Cinepak Video Codec. When parsing the data in the MDAT atom, there exists a signedness error which leads to a heap overflow. When this occurs it can be further leveraged to execute arbitrary code under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT3403

## Disclosure Timeline

- 2008-06-23 - Vulnerability reported to vendor
- 2009-01-21 - Coordinated public release of advisory
