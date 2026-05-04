# ZDI-22-791: Apple macOS SCPT File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-791
- **ZDI-CAN:** ZDI-CAN-16073
- **Date:** 2022-05-26
- **CVE:** CVE-2022-26697
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Qi Sun and Robert Ai of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-791/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple macOS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the AppleScript framework. Crafted data in a SCPT file can trigger a read past the end of an allocated data structure. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-al/HT213257

## Disclosure Timeline

- 2021-12-03 - Vulnerability reported to vendor
- 2022-05-26 - Coordinated public release of advisory
