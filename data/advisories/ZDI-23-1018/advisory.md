# ZDI-23-1018: Apple Safari DFG Fixup Phase Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1018
- **ZDI-CAN:** ZDI-CAN-19555
- **Date:** 2023-08-04
- **CVE:** CVE-2023-28198
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** hazbinhotel
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1018/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the DFG fixup phase. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-ca/HT213670

## Disclosure Timeline

- 2022-12-29 - Vulnerability reported to vendor
- 2023-08-04 - Coordinated public release of advisory
