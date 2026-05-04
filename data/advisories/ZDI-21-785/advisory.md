# ZDI-21-785: Apple macOS ImageIO PICT File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-785
- **ZDI-CAN:** ZDI-CAN-13232
- **Date:** 2021-07-12
- **CVE:** CVE-2021-30701
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Jzhu
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-785/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. Interaction with the ImageIO library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the ImageIO framework. Crafted data in a PICT image can trigger a write past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/HT212529

## Disclosure Timeline

- 2021-05-05 - Vulnerability reported to vendor
- 2021-07-12 - Coordinated public release of advisory
