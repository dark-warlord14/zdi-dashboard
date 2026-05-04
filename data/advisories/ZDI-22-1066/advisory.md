# ZDI-22-1066: Apple macOS LaunchServices Sandbox Escape Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1066
- **ZDI-CAN:** ZDI-CAN-15588
- **Date:** 2022-08-15
- **CVE:** CVE-2022-26696
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Wojciech Reguła (@_r3ggi)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1066/
## Vulnerability Details

This vulnerability allows remote attackers to escape the sandbox on affected installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of XPC messages in the LaunchServices component. A crafted message can trigger execution of a privileged operation. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the current user.

## Additional Details

ZDI-CAN-15588 / CVE-2022-26696 was addressed in macOS Monterey 12.4.

## Disclosure Timeline

- 2021-12-22 - Vulnerability reported to vendor
- 2022-08-15 - Coordinated public release of advisory
