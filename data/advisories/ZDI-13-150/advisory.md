# ZDI-13-150: Apple QuickTime PICT Image LongComment Opcode Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-150
- **ZDI-CAN:** ZDI-CAN-1620
- **Date:** 2013-06-27
- **CVE:** CVE-2013-0975
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** Tobias Klein
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-150/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way QuickTime handles the LongComment PICT opcode. It converts an unsigned 16 bit value into a signed 32 bit value after it performs some mathematical operations on it. This value is later used as a size parameter for a memory copy function that copies from the file onto the heap. An attacker can leverage the situation to achieve remote code execution under the context of the user currently logged in.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2012-11-19 - Vulnerability reported to vendor
- 2013-06-27 - Coordinated public release of advisory
