# ZDI-19-287: Apple macOS StreamFlatFont Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-287
- **ZDI-CAN:** ZDI-CAN-7442
- **Date:** 2019-03-26
- **CVE:** CVE-2019-8517
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** riusksk of VulWar Corp
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-287/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Apple macOS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the StreamFlatFont method. Crafted data in a TTF file can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT209599

## Disclosure Timeline

- 2018-11-04 - Vulnerability reported to vendor
- 2019-03-26 - Coordinated public release of advisory
