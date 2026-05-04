# ZDI-19-856: Apple macOS parseText1Fast Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-856
- **ZDI-CAN:** ZDI-CAN-8584
- **Date:** 2019-10-04
- **CVE:** CVE-2019-8657
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** riusksk of VulWar Corp
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-856/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple macOS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parseText1Fast function. Crafted data in a DOC file can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT210348

## Disclosure Timeline

- 2019-05-31 - Vulnerability reported to vendor
- 2019-10-04 - Coordinated public release of advisory
