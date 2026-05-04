# ZDI-20-1408: Apple macOS process_token_BlitLibSetup2D Out-Of-Bounds Access Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1408
- **ZDI-CAN:** ZDI-CAN-11123
- **Date:** 2020-12-09
- **CVE:** CVE-2020-10015
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** ABC Research s.r.o.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1408/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the AppleIntelKBLGraphics kext. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated array. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the kernel.

## Additional Details

This issue was addressed in macOS Big Sur 11.0.1 and iOS 14.

## Disclosure Timeline

- 2020-07-15 - Vulnerability reported to vendor
- 2020-12-09 - Coordinated public release of advisory
