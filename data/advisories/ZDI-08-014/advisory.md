# ZDI-08-014: Apple Quicktime Multiple Opcode Memory Corruption Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-08-014
- **ZDI-CAN:** ZDI-CAN-267
- **Date:** 2008-04-03
- **CVE:** CVE-2008-1019
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** bugfree
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-014/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must open a malicious file. The specific flaw exists in the quickTime.qts while parsing corrupted .pict files. The module contains a vulnerable memory copy loop which searches for a terminator value. When this value is changed or omitted, a heap corruption occurs allowing the execution of arbitrary code.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1241

## Disclosure Timeline

- 2008-02-07 - Vulnerability reported to vendor
- 2008-04-03 - Coordinated public release of advisory
