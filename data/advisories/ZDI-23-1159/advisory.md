# ZDI-23-1159: Apple macOS KTX Image Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1159
- **ZDI-CAN:** ZDI-CAN-19367
- **Date:** 2023-08-22
- **CVE:** CVE-2023-27939
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** jzhu
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1159/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple macOS. Interaction with the ImageIO framework is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the ImageIO framework. Crafted data in a KTX image can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-ca/HT213670

## Disclosure Timeline

- 2022-12-16 - Vulnerability reported to vendor
- 2023-08-22 - Coordinated public release of advisory
