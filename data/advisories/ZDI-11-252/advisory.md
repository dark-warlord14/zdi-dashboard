# ZDI-11-252: Apple QuickTime PICT Image PnSize Opcode Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-252
- **ZDI-CAN:** ZDI-CAN-1164
- **Date:** 2011-08-08
- **CVE:** CVE-2011-0257
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Matt "j00ru" Jurczyk
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-252/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Quicktime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Quicktime handles the PnSize PICT opcode. It converts an unsigned 16 bit value into a signed 32 bit value. This value is later used as the size parameter for a memory copy function that copies from the file onto the stack. The results in a stack based buffer overflow that allows for remote code execution under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4826

## Disclosure Timeline

- 2011-04-11 - Vulnerability reported to vendor
- 2011-08-08 - Coordinated public release of advisory
