# ZDI-19-832: QuickTime get_by_tree Memory Corruption Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-832
- **ZDI-CAN:** ZDI-CAN-8091
- **Date:** 2019-09-17
- **CVE:** CVE-2019-8585
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** riusksk of VulWar Corp
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-832/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the AudioCodecs module. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT210119

## Disclosure Timeline

- 2019-03-08 - Vulnerability reported to vendor
- 2019-09-17 - Coordinated public release of advisory
