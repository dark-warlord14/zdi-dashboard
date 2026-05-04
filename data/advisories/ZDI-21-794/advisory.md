# ZDI-21-794: Apple macOS CVMServer Integer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-794
- **ZDI-CAN:** ZDI-CAN-13345
- **Date:** 2021-07-13
- **CVE:** CVE-2021-30724
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Mickey Jin (@patch1t) of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-794/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the CVMServer daemon. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before writing to memory. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

https://support.apple.com/HT212529

## Disclosure Timeline

- 2021-03-17 - Vulnerability reported to vendor
- 2021-07-13 - Coordinated public release of advisory
- 2021-07-13 - Advisory Updated
