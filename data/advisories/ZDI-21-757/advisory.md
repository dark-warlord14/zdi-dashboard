# ZDI-21-757: Apple macOS AudioToolboxCore AAC File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-757
- **ZDI-CAN:** ZDI-CAN-13118
- **Date:** 2021-06-25
- **CVE:** CVE-2021-30685
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Mickey Jin of Trend Micro Mobile Security Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-757/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple macOS. Interaction with the AudioToolboxCore library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the AudioToolboxCore framework. Crafted data in a AAC file can trigger a read past the end of an allocated data structure. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/HT212529

## Disclosure Timeline

- 2021-02-03 - Vulnerability reported to vendor
- 2021-06-25 - Coordinated public release of advisory
