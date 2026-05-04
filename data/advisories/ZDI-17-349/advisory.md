# ZDI-17-349: (Pwn2Own) Apple macOS WindowServer _XGetWindowMovementGroup Stack-based Buffer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-349
- **ZDI-CAN:** ZDI-CAN-4600
- **Date:** 2017-05-15
- **CVE:** CVE-2017-2541
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Richard Zhu (fluorescence)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-349/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the WindowServer process. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to escalate privileges under the context of the WindowServer.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/kb/HT201222

## Disclosure Timeline

- 2017-03-15 - Vulnerability reported to vendor
- 2017-05-15 - Coordinated public release of advisory
