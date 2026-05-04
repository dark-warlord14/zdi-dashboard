# ZDI-17-364: (Pwn2Own) Apple macOS AppleMultitouchDevice Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-364
- **ZDI-CAN:** ZDI-CAN-4610
- **Date:** 2017-05-18
- **CVE:** CVE-2017-2543
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** 360 Vulcan Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-364/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of the AppleMultitouchDevice kext. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code under the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT207797

## Disclosure Timeline

- 2017-03-17 - Vulnerability reported to vendor
- 2017-05-18 - Coordinated public release of advisory
