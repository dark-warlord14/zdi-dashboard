# ZDI-25-193: Apple macOS CoreText Font Glyphs Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-193
- **ZDI-CAN:** ZDI-CAN-26154
- **Date:** 2025-04-01
- **CVE:** CVE-2025-24182
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Hossein Lotfi (@hosselot) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-193/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple macOS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of font glyphs within the CoreText framework. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/122373

## Disclosure Timeline

- 2025-01-08 - Vulnerability reported to vendor
- 2025-04-01 - Coordinated public release of advisory
- 2025-04-01 - Advisory Updated
