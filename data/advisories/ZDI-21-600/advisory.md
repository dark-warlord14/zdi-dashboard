# ZDI-21-600: Apple macOS libFontParser OTF Font Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-600
- **ZDI-CAN:** ZDI-CAN-12776
- **Date:** 2021-05-20
- **CVE:** CVE-2021-1881
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Mickey Jin of Trend Micro Mobile Security Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-600/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple macOS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the GetFDIndex function in libFontParser. Crafted data in an OTF font can trigger a read past the end of an allocated data structure. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/HT212325

## Disclosure Timeline

- 2021-01-08 - Vulnerability reported to vendor
- 2021-05-20 - Coordinated public release of advisory
- 2021-05-20 - Advisory Updated
