# ZDI-23-645: Apple macOS AppleScript UASIsConstant SCPT File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-645
- **ZDI-CAN:** ZDI-CAN-17359
- **Date:** 2023-05-17
- **CVE:** CVE-2022-32797
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Mickey Jin (@patch1t) of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-645/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple macOS. Interaction with the AppleScript library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the AppleScript framework. Crafted data in an SCPT file can trigger a read past the end of an allocated data structure. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT213345

## Disclosure Timeline

- 2022-06-06 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
