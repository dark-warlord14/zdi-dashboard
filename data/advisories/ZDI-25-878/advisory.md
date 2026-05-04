# ZDI-25-878: Apple macOS AppleIntelKBLGraphics Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-878
- **ZDI-CAN:** ZDI-CAN-26523
- **Date:** 2025-08-28
- **CVE:** CVE-2025-43284
- **CVSS:** 6.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-878/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the AppleIntelKBLGraphics kext. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute code in the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/124149

## Disclosure Timeline

- 2025-04-04 - Vulnerability reported to vendor
- 2025-08-28 - Coordinated public release of advisory
- 2026-02-04 - Advisory Updated
