# ZDI-16-205: Apple OS X IOGraphicsFamily Untrusted Pointer Dereference Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-205
- **ZDI-CAN:** ZDI-CAN-3453
- **Date:** 2016-03-22
- **CVE:** CVE-2016-1747
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Juwei Lin of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-205/
## Vulnerability Details

This vulnerability allows local attackers to elevate privileges on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must open a malicious file. The specific flaw exists within the IOGraphicsFamily interface. The issue lies failure to validate user-supplied function addresses prior to using them. An attacker can leverage this to escalate their privileges and execute code under the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT206167

## Disclosure Timeline

- 2015-12-17 - Vulnerability reported to vendor
- 2016-03-22 - Coordinated public release of advisory
