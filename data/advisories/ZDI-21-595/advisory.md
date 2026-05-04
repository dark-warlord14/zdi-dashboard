# ZDI-21-595: Apple macOS AppleIntelKBLGraphics IOCTL 0x30005 Out-Of-Bounds Write Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-595
- **ZDI-CAN:** ZDI-CAN-12196
- **Date:** 2021-05-20
- **CVE:** CVE-2021-1834
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** ABC Research s.r.o.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-595/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of IOCTL 0x30005 in the AppleIntelKBLGraphics kext. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated data structure. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/HT212325

## Disclosure Timeline

- 2020-12-18 - Vulnerability reported to vendor
- 2021-05-20 - Coordinated public release of advisory
- 2021-05-20 - Advisory Updated
