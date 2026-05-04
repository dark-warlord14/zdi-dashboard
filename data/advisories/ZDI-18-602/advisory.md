# ZDI-18-602: Apple macOS APFS methodVolumeCreate Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-602
- **ZDI-CAN:** ZDI-CAN-6132
- **Date:** 2018-07-10
- **CVE:** CVE-2018-4268
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Mac
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-602/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of APFS. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute code as the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT208937

## Disclosure Timeline

- 2018-04-25 - Vulnerability reported to vendor
- 2018-07-10 - Coordinated public release of advisory
- 2018-07-10 - Advisory Updated
