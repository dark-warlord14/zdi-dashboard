# ZDI-20-1182: Apple macOS AppleVPA JPEG Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1182
- **ZDI-CAN:** ZDI-CAN-11106
- **Date:** 2020-09-16
- **CVE:** CVE-2020-9887
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Mickey Jin of Trend Micro Mobile Security Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1182/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. Interaction with the ImageIO library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the AppleVPA framework. Crafted data in a JPEG image can trigger a write past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/HT211289

## Disclosure Timeline

- 2020-05-19 - Vulnerability reported to vendor
- 2020-09-16 - Coordinated public release of advisory
