# ZDI-08-019: Apple QuickTime Malformed VR obji Atom Parsing Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-019
- **ZDI-CAN:** ZDI-CAN-272
- **Date:** 2008-04-03
- **CVE:** CVE-2008-1022
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-019/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must open a malicious file. The specific flaw exists in the parsing of the QuickTime VR 'obji' atom. When the size of the atom is set to 0, a stack overflow condition occurs resulting in the execution of arbitrary code.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1241

## Disclosure Timeline

- 2008-02-07 - Vulnerability reported to vendor
- 2008-04-03 - Coordinated public release of advisory
