# ZDI-16-431: Apple OS X WindowServer Memory Corruption Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-431
- **ZDI-CAN:** ZDI-CAN-3776
- **Date:** 2016-07-20
- **CVE:** CVE-2016-4639
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** e048b7039acc9483d42ca9ef197bd909
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-431/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within CoreGraphics. By interacting with PKGTransactionWillSwitchSpaces, an attacker can cause a memory corruption condition. An attacker could leverage this vulnerability to execute arbitrary code under the context of the WindowServer.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT206903

## Disclosure Timeline

- 2016-05-20 - Vulnerability reported to vendor
- 2016-07-20 - Coordinated public release of advisory
