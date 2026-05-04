# ZDI-06-007: Microsoft Windows Address Book (WAB) File Format Parsing Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-007
- **ZDI-CAN:** ZDI-CAN-002
- **Date:** 2006-04-11
- **CVE:** CVE-2006-0014
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** File Format Vulnerability
- **Credit:** Stuart Pearson - Computer Terrorism (UK)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-007/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of the Microsoft Windows operating system. User interaction is required to exploit this vulnerability. The specific flaw exists during the parsing of malformed Windows Address Book (.WAB) files. Modification of the length value of certain Unicode strings within this file format results in an exploitable heap corruption.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/Bulletin/MS06-016.mspx

## Disclosure Timeline

- 2005-09-20 - Vulnerability reported to vendor
- 2006-04-11 - Coordinated public release of advisory
