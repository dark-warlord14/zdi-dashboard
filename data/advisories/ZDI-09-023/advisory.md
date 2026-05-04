# ZDI-09-023: Apple OS X ATSServer Compact Font Format Parsing Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-023
- **ZDI-CAN:** ZDI-CAN-462
- **Date:** 2009-05-13
- **CVE:** CVE-2009-0154
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Charlie Miller, Independent Security Evaluators
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-023/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw appears to exist in the ATSServer font server upon parsing of malicious Compact Font Format files. A boundary condition exists in the parsing of internal dictionaries that can lead to a memory corruption allowing the execution of arbitrary code.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT3549

## Disclosure Timeline

- 2009-03-19 - Vulnerability reported to vendor
- 2009-05-13 - Coordinated public release of advisory
