# ZDI-20-1394: Apple Safari TextNode Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1394
- **ZDI-CAN:** ZDI-CAN-11498
- **Date:** 2020-12-03
- **CVE:** CVE-2020-9950
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** cc
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1394/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of TextNode objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT211844

## Disclosure Timeline

- 2020-08-05 - Vulnerability reported to vendor
- 2020-12-03 - Coordinated public release of advisory
