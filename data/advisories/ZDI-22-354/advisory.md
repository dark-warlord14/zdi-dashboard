# ZDI-22-354: Apple macOS CoreML MLMODEL File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-354
- **ZDI-CAN:** ZDI-CAN-13804
- **Date:** 2022-02-16
- **CVE:** CVE-2021-30825
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** hjy79425575
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-354/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple macOS. Interaction with the CoreML library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the CoreML framework. Crafted data in an mlmodel file can trigger a read past the end of an allocated data structure. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/HT212814

## Disclosure Timeline

- 2021-06-04 - Vulnerability reported to vendor
- 2022-02-16 - Coordinated public release of advisory
