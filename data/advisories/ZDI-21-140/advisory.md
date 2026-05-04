# ZDI-21-140: Apple macOS CoreText ApplyContextPosFormat2 TTF Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-140
- **ZDI-CAN:** ZDI-CAN-12153
- **Date:** 2021-02-04
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Mickey Jin of Trend Micro Mobile Security Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-140/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. Interaction with the CoreText library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the parsing of TTF fonts. Crafted data in a TTF file can trigger an overflow of a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT212147

## Disclosure Timeline

- 2020-10-21 - Vulnerability reported to vendor
- 2021-02-04 - Coordinated public release of advisory
