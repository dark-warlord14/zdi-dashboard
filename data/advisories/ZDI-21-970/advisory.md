# ZDI-21-970: Apple macOS CoreText TTF File Parsing Integer Overflow Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-970
- **ZDI-CAN:** ZDI-CAN-13875
- **Date:** 2021-08-11
- **CVE:** CVE-2021-30789
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Mickey Jin (@patch1t) of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-970/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple macOS. Interaction with the CoreText library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the CoreText framework. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before reading memory. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/HT212602

## Disclosure Timeline

- 2021-05-19 - Vulnerability reported to vendor
- 2021-08-11 - Coordinated public release of advisory
