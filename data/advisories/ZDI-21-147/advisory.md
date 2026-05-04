# ZDI-21-147: Apple macOS ImageIO EXR Parsing Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-147
- **ZDI-CAN:** ZDI-CAN-12627
- **Date:** 2021-02-04
- **CVE:** CVE-2021-1743
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Mickey Jin & Junzhi Lu of Trend Micro Mobile Security Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-147/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. Interaction with the ImageIO library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the ImageIO framework. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before reading memory. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT212147

## Disclosure Timeline

- 2020-12-16 - Vulnerability reported to vendor
- 2021-02-04 - Coordinated public release of advisory
