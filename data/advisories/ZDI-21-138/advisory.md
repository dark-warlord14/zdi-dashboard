# ZDI-21-138: Apple macOS libFontParser TTF Parsing Integer Underflow Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-138
- **ZDI-CAN:** ZDI-CAN-11876
- **Date:** 2021-02-04
- **CVE:** CVE-2021-1775
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Mickey Jin & Qi Sun of Trend Micro Mobile Security Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-138/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple macOS. Interaction with the libFontParser library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the parsing of TTF fonts. The issue results from the lack of proper validation of user-supplied data, which can result in an integer underflow before reading from memory. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT212147

## Disclosure Timeline

- 2020-09-04 - Vulnerability reported to vendor
- 2021-02-04 - Coordinated public release of advisory
