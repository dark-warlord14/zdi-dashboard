# ZDI-19-422: Apple macOS apfs Volume Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-422
- **ZDI-CAN:** ZDI-CAN-7344
- **Date:** 2019-04-29
- **CVE:** CVE-2019-8534
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Mac
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-422/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of APFS volumes. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute code as the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/HT209600

## Disclosure Timeline

- 2018-12-27 - Vulnerability reported to vendor
- 2019-04-29 - Coordinated public release of advisory
