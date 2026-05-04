# ZDI-16-639: Apple OS X WindowServer _XSetDictionaryForCurrentSession Type Confusion Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-639
- **ZDI-CAN:** ZDI-CAN-3773
- **Date:** 2016-12-15
- **CVE:** CVE-2016-4638
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** e048b7039acc9483d42ca9ef197bd909
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-639/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Apple OS X. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the CoreGraphics module. The issue lies in the failure to properly validate user-supplied data which can result in a type confusion condition. An attacker can leverage this vulnerability to escalate privileges under the context of WindowServer.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT206903

## Disclosure Timeline

- 2016-06-14 - Vulnerability reported to vendor
- 2016-12-15 - Coordinated public release of advisory
