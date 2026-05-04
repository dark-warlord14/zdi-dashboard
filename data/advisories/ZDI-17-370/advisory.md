# ZDI-17-370: (Pwn2Own) Apple macOS nsurlstoraged Null Pointer Dereference Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-370
- **ZDI-CAN:** ZDI-CAN-4583
- **Date:** 2017-05-30
- **CVE:** N/A
- **CVSS:** 2.1
- **CVSS Vector:** AV:L/AC:L/Au:N/C:N/I:N/A:P
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Niklas Baumstark and Samuel Gro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-370/
## Vulnerability Details

This vulnerability allows local attackers to trigger a denial-of-service condition on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the nsurlstoraged service. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to cause the service to restart.

## Additional Details

Regarding ZDI-CAN-4583, this was addressed by a mitigation. Multiple denial of service issues were addressed through improved memory handling. The finder has been acknowledged in our 'Additional recognition' section on the macOS Sierra 10.12.5 advisory at https://support.apple.com/HT207797 .

## Disclosure Timeline

- 2017-03-17 - Vulnerability reported to vendor
- 2017-05-30 - Coordinated public release of advisory
