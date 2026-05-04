# ZDI-21-597: Apple macOS QuartzCore Type Confusion Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-597
- **ZDI-CAN:** ZDI-CAN-12157
- **Date:** 2021-05-20
- **CVE:** CVE-2021-30745
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Peter Nguyen of STAR Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-597/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the QuartzCore Framework. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of WindowServer.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/HT212326

## Disclosure Timeline

- 2020-12-18 - Vulnerability reported to vendor
- 2021-05-20 - Coordinated public release of advisory
- 2021-05-20 - Advisory Updated
