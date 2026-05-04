# ZDI-14-326: Apple QuickTime MIDI Heap Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-326
- **ZDI-CAN:** ZDI-CAN-2238
- **Date:** 2014-09-22
- **CVE:** CVE-2014-4350
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** s3tm3m
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-326/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of MIDI events. An arithmetic overflow in the handling of the sizes of certain events allows for an attacker to overflow a heap buffer. An attacker could use this to execute arbitrary code in the context of the QuickTime process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2014-04-03 - Vulnerability reported to vendor
- 2014-09-22 - Coordinated public release of advisory
