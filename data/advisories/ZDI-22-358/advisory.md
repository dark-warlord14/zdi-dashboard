# ZDI-22-358: Apple macOS ModelIO ABC File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-358
- **ZDI-CAN:** ZDI-CAN-15171
- **Date:** 2022-02-16
- **CVE:** CVE-2021-30979
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Mickey Jin (@patch1t) of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-358/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. Interaction with the ModelIO library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the ModelIO framework. Crafted data in a ABC file can trigger an overflow of a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/HT212979

## Disclosure Timeline

- 2021-09-01 - Vulnerability reported to vendor
- 2022-02-16 - Coordinated public release of advisory
