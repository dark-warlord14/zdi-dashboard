# ZDI-18-1338: (Pwn2Own) Apple macOS launchd Improper Access Check Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1338
- **ZDI-CAN:** ZDI-CAN-5820
- **Date:** 2018-11-05
- **CVE:** CVE-2018-4404
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Samuel Gross (saelo)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1338/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of Mach messages to the Dock. The issue results from the lack of proper validation of the client prior to spawning a process. An attacker can leverage this vulnerability to execute code within the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT208848

## Disclosure Timeline

- 2018-04-07 - Vulnerability reported to vendor
- 2018-11-05 - Coordinated public release of advisory
- 2018-11-05 - Advisory Updated
