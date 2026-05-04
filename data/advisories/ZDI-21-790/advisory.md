# ZDI-21-790: (Pwn2Own) Apple macOS process_token_VPHAL Out-Of-Bounds Write Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-790
- **ZDI-CAN:** ZDI-CAN-13596
- **Date:** 2021-07-13
- **CVE:** CVE-2021-30735
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** ret2systems
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-790/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the AppleIntelKBLGraphics kext. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated data structure. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/HT212529

## Disclosure Timeline

- 2021-04-27 - Vulnerability reported to vendor
- 2021-07-13 - Coordinated public release of advisory
