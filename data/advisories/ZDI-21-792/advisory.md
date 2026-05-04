# ZDI-21-792: Apple macOS vImage PICT File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-792
- **ZDI-CAN:** ZDI-CAN-13807
- **Date:** 2021-07-13
- **CVE:** CVE-2021-30701
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Mickey Jin (@patch1t) of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-792/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. Interaction with the vImage library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the vImage framework. Crafted data in a PICT file can trigger a write past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/HT212529

## Disclosure Timeline

- 2021-05-05 - Vulnerability reported to vendor
- 2021-07-13 - Coordinated public release of advisory
