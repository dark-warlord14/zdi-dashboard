# ZDI-19-934: Apple macOS AppleIntelCFLGraphicsFramebuffer.kext Untrusted Pointer Dereference Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-934
- **ZDI-CAN:** ZDI-CAN-8828
- **Date:** 2019-10-31
- **CVE:** CVE-2019-8755 , CVE-2019-8758
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Lilang Wu and Moony Li of TrendMicro Mobile Security Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-934/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within AppleIntelCFLGraphicsFramebuffer.kext. The issue results from the lack of proper validation of a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT210634

## Disclosure Timeline

- 2019-06-28 - Vulnerability reported to vendor
- 2019-10-31 - Coordinated public release of advisory
