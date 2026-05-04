# ZDI-21-948: Apple macOS ModelIO USD File Parsing Out-Of-Bounds Write Remote Code Execute Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-948
- **ZDI-CAN:** ZDI-CAN-14011
- **Date:** 2021-08-05
- **CVE:** CVE-2021-30796
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Mickey Jin (@patch1t) of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-948/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. Interaction with the ModelIO library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the ModelIO framework. Crafted data in a USD file can trigger a write past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT212602

## Disclosure Timeline

- 2021-06-04 - Vulnerability reported to vendor
- 2021-08-05 - Coordinated public release of advisory
