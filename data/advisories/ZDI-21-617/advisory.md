# ZDI-21-617: Apple macOS ImageIO PICT File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-617
- **ZDI-CAN:** ZDI-CAN-12626
- **Date:** 2021-06-02
- **CVE:** CVE-2021-1838
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Mickey Jin & Junzhi Lu of Trend Micro Mobile Security Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-617/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple macOS. Interaction with the ImageIO library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the ImageIO framework. Crafted data in a PICT image can trigger a read past the end of an allocated data structure. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/HT212146

## Disclosure Timeline

- 2020-12-16 - Vulnerability reported to vendor
- 2021-06-02 - Coordinated public release of advisory
