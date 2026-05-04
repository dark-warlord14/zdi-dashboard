# ZDI-17-360: (Pwn2Own) Apple Safari WebSQL Type Confusion Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-360
- **ZDI-CAN:** ZDI-CAN-4593
- **Date:** 2017-05-18
- **CVE:** CVE-2017-6991
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Chaitin Security Research Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-360/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of WebSQL. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this in conjunction with other vulnerabilities to execute code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT207798

## Disclosure Timeline

- 2017-03-17 - Vulnerability reported to vendor
- 2017-05-18 - Coordinated public release of advisory
