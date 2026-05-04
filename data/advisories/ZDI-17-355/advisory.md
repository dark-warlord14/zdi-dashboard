# ZDI-17-355: (Pwn2Own) Apple macOS WindowServer XSetWindowListBrightness Out-Of-Bounds Access Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-355
- **ZDI-CAN:** ZDI-CAN-4624
- **Date:** 2017-05-18
- **CVE:** CVE-2017-2548
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Team Sniper (Keen Team and PC Manager)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-355/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the WindowServer process. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated buffer. An attacker can leverage this vulnerability to escalate privileges under the context of the WindowServer.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT207797

## Disclosure Timeline

- 2017-03-17 - Vulnerability reported to vendor
- 2017-05-18 - Coordinated public release of advisory
