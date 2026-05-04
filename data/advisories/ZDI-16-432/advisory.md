# ZDI-16-432: Apple OS X WindowServer _XFlushRegion Out-Of-Bounds Read Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-432
- **ZDI-CAN:** ZDI-CAN-3771
- **Date:** 2016-07-20
- **CVE:** CVE-2016-4652
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:N/A:P
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** aca055c25829115b84ad07e72a4eff16
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-432/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of Apple OS X. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the CoreGraphics module. The issue lies in the failure to properly validate user-supplied data which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges in the context of WindowServer.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT206903

## Disclosure Timeline

- 2016-06-14 - Vulnerability reported to vendor
- 2016-07-20 - Coordinated public release of advisory
