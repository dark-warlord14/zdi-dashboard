# ZDI-21-396: Apple macOS AppleIntelKBLGraphics IOCTL 0x30000 Out-Of-Bounds Write Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-396
- **ZDI-CAN:** ZDI-CAN-11960
- **Date:** 2021-03-30
- **CVE:** CVE-2020-27897
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** ABC Research s.r.o.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-396/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of IOCTL 0x30000 in the AppleIntelKBLGraphics kext. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated data structure. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT212011

## Disclosure Timeline

- 2020-09-30 - Vulnerability reported to vendor
- 2021-03-30 - Coordinated public release of advisory
