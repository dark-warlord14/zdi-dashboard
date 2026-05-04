# ZDI-23-1226: Apple macOS ImageIO EXR File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1226
- **ZDI-CAN:** ZDI-CAN-20043
- **Date:** 2023-08-25
- **CVE:** CVE-2023-32384
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Meysam Firouzi @R00tkitsmm
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1226/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. Interaction with the ImageIO library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the ImageIO framework. Crafted data in an EXR image can trigger a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT213757

## Disclosure Timeline

- 2023-02-08 - Vulnerability reported to vendor
- 2023-08-25 - Coordinated public release of advisory
