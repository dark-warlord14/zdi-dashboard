# ZDI-10-035: Apple QuickTime genl Atom Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-035
- **ZDI-CAN:** ZDI-CAN-461
- **Date:** 2010-04-02
- **CVE:** CVE-2010-0526
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-035/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must open a malicious file. The specific flaw exists in QuickTimeMPEG.qtx and results when QuickTime attempts to parse a malformed 'genl' atom that may be present in any QuickTime media file. A heap overflow is caused when QuickTime fails to perform proper bounds checking on the amount of data copied to the heap by a set of nested loops which can result in arbitrary code execution.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4077

## Disclosure Timeline

- 2009-03-26 - Vulnerability reported to vendor
- 2010-04-02 - Coordinated public release of advisory
