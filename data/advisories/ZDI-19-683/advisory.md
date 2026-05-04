# ZDI-19-683: Apple Safari operationPutByValOptimize Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-683
- **ZDI-CAN:** ZDI-CAN-8489
- **Date:** 2019-07-24
- **CVE:** CVE-2019-8658
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** akayn
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-683/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the operationPutByValOptimize function. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT210353

## Disclosure Timeline

- 2019-05-31 - Vulnerability reported to vendor
- 2019-07-24 - Coordinated public release of advisory
