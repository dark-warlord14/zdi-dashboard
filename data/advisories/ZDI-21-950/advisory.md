# ZDI-21-950: Apple macOS AppKit PDF File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-950
- **ZDI-CAN:** ZDI-CAN-13578
- **Date:** 2021-08-09
- **CVE:** CVE-2021-30790
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** hjy79425575
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-950/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple macOS. Interaction with the AppKit library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the AppKit framework. Crafted data in a PDF file can trigger a read past the end of an allocated data structure. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT212602

## Disclosure Timeline

- 2021-05-07 - Vulnerability reported to vendor
- 2021-08-09 - Coordinated public release of advisory
