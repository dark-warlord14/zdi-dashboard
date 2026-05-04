# ZDI-24-206: Apple macOS ImageIO MPO Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-206
- **ZDI-CAN:** ZDI-CAN-21769
- **Date:** 2024-02-26
- **CVE:** CVE-2023-42888
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-206/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple macOS. Interaction with the ImageIO library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the ImageIO framework. Crafted data in an MPO image can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/HT214036

## Disclosure Timeline

- 2023-07-27 - Vulnerability reported to vendor
- 2024-02-26 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
