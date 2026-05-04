# ZDI-21-143: Apple macOS ModelIO USD Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-143
- **ZDI-CAN:** ZDI-CAN-12233
- **Date:** 2021-02-04
- **CVE:** CVE-2021-1763
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Mickey Jin of Trend Micro Mobile Security Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-143/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. Interaction with the ModelIO library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the ModelIO framework. Crafted data in a USD file can trigger an overflow of a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT212147

## Disclosure Timeline

- 2020-10-28 - Vulnerability reported to vendor
- 2021-02-04 - Coordinated public release of advisory
