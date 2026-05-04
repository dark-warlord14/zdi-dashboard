# ZDI-22-355: Apple macOS CVMServer Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-355
- **ZDI-CAN:** ZDI-CAN-14040
- **Date:** 2022-02-16
- **CVE:** CVE-2021-30832
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Mickey Jin (@patch1t) of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-355/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the CVMServer daemon. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/HT212804

## Disclosure Timeline

- 2021-06-04 - Vulnerability reported to vendor
- 2022-02-16 - Coordinated public release of advisory
