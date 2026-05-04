# ZDI-09-005: Apple QuickTime VR Track Header Atom Heap Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-005
- **ZDI-CAN:** ZDI-CAN-382
- **Date:** 2009-01-21
- **CVE:** CVE-2009-0002
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-005/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Apple Quicktime Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of 'tkhd' atoms found inside QuickTimeVR files. Improper validation of the transform matrix data results in a heap chunk header overwrite leading to arbitrary code execution under the context of the currently logged in user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT3403

## Disclosure Timeline

- 2008-09-16 - Vulnerability reported to vendor
- 2009-01-21 - Coordinated public release of advisory
