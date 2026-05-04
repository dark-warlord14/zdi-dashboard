# ZDI-10-250: Apple Quicktime rec Chunk Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-250
- **ZDI-CAN:** ZDI-CAN-739
- **Date:** 2010-11-10
- **CVE:** CVE-2010-3789
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-250/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Quicktime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the code responsible for parsing rec chunks within an AVI media file. By modifying specific values within the data structure a heap corruption condition can be triggered. An attacker can abuse this to execute arbitrary code under the context of the user running QuickTime.

## Additional Details

Fixed in Mac OS X 10.6.5: http://support.apple.com/kb/HT4435 QuickTime 7.6.9: http://support.apple.com/kb/HT4447

## Disclosure Timeline

- 2010-04-13 - Vulnerability reported to vendor
- 2010-11-10 - Coordinated public release of advisory
