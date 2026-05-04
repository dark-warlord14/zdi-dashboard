# ZDI-25-194: Apple macOS AppleIntelKBLGraphics Time-Of-Check Time-Of-Use Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-194
- **ZDI-CAN:** ZDI-CAN-26063
- **Date:** 2025-04-01
- **CVE:** CVE-2025-24256
- **CVSS:** 6.4
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:N/A:L
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-194/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the AppleIntelKBLGraphics kext. he issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/122373

## Disclosure Timeline

- 2025-02-13 - Vulnerability reported to vendor
- 2025-04-01 - Coordinated public release of advisory
- 2025-04-01 - Advisory Updated
