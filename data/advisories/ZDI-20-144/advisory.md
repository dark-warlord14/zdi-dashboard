# ZDI-20-144: Apple Safari SimpleLineLayout Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-144
- **ZDI-CAN:** ZDI-CAN-9399
- **Date:** 2020-01-27
- **CVE:** CVE-2019-8835
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-144/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the SimpleLineLayout object. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/HT210790

## Disclosure Timeline

- 2019-09-27 - Vulnerability reported to vendor
- 2020-01-27 - Coordinated public release of advisory
