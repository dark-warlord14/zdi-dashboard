# ZDI-18-576: Apple macOS Dock Service DSSetItemTitle Uninitialized Pointer Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-576
- **ZDI-CAN:** ZDI-CAN-6123
- **Date:** 2018-06-11
- **CVE:** CVE-2018-4196
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** G. Geshev
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-576/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of Mach messages to the Dock. The issue results from the lack of proper initialization of a pointer prior to accessing it. An attacker can leverage this vulnerability to execute code within the context of the Dock process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-ca/HT208849

## Disclosure Timeline

- 2018-04-25 - Vulnerability reported to vendor
- 2018-06-11 - Coordinated public release of advisory
- 2018-06-11 - Advisory Updated
