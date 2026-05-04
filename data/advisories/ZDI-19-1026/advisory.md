# ZDI-19-1026: Apple macOS apfs Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-1026
- **ZDI-CAN:** ZDI-CAN-8767
- **Date:** 2019-12-19
- **CVE:** CVE-2019-8835
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Mac
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-1026/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the apfs kernel extension. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this to escalate privileges and execute code in the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT210792

## Disclosure Timeline

- 2019-08-07 - Vulnerability reported to vendor
- 2019-12-19 - Coordinated public release of advisory
