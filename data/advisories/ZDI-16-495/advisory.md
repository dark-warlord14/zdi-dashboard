# ZDI-16-495: Apple OS X IOHDIXController Untrusted Pointer Dereference Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-495
- **ZDI-CAN:** ZDI-CAN-3558
- **Date:** 2016-08-29
- **CVE:** CVE-2016-1808
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Moony Li and Jack Tang of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-495/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must open a malicious file. The specific flaw exists within the IOHDIXController interface. The issue lies with the failure to validate user-supplied function addresses prior to using them. An attacker can leverage this vulnerability to escalate privileges and execute code under the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT206567

## Disclosure Timeline

- 2016-02-12 - Vulnerability reported to vendor
- 2016-08-29 - Coordinated public release of advisory
