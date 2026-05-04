# ZDI-25-1179: Foxit PDF Reader U3D File Parsing Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1179
- **ZDI-CAN:** ZDI-CAN-28532
- **Date:** 2025-12-19
- **CVE:** CVE-2025-66498
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Foxit
- **Affected Products:** PDF Reader
- **Credit:** Mat Powell of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1179/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Foxit PDF Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of U3D files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

https://www.foxit.com/support/security-bulletins.html

## Disclosure Timeline

- 2025-11-04 - Vulnerability reported to vendor
- 2025-12-19 - Coordinated public release of advisory
- 2025-12-19 - Advisory Updated
