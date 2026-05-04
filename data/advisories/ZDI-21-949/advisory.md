# ZDI-21-949: Apple macOS CoreGraphics JPG File Parsing Out-of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-949
- **ZDI-CAN:** ZDI-CAN-13577
- **Date:** 2021-08-09
- **CVE:** CVE-2021-30790
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** hjy79425575
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-949/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. Interaction with the CoreGraphics library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the parsing of JPG files. Crafted data in a JPG file can trigger a write past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT212602

## Disclosure Timeline

- 2021-05-05 - Vulnerability reported to vendor
- 2021-08-09 - Coordinated public release of advisory
