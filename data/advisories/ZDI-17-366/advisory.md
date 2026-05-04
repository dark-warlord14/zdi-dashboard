# ZDI-17-366: (Pwn2Own) Apple Safari WebSQL optimize Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-366
- **ZDI-CAN:** ZDI-CAN-4591
- **Date:** 2017-05-30
- **CVE:** CVE-2017-6983
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Chaitin Security Research Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-366/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of WebSQL. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT207798

## Disclosure Timeline

- 2017-03-17 - Vulnerability reported to vendor
- 2017-05-30 - Coordinated public release of advisory
