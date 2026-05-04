# ZDI-09-006: Apple QuickTime AVI Header nBlockAlign Heap Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-006
- **ZDI-CAN:** ZDI-CAN-393
- **Date:** 2009-01-21
- **CVE:** CVE-2009-0003
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-006/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of AVI files. When the AVI header contains a malformed nBlockAlign value in the _WAVEFORMATEX structure, a heap overflow may occur which can be leveraged to execute arbitrary code under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT3403

## Disclosure Timeline

- 2008-10-15 - Vulnerability reported to vendor
- 2009-01-21 - Coordinated public release of advisory
