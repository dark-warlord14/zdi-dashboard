# ZDI-21-1207: Foxit PDF Reader PDF File Parsing Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1207
- **ZDI-CAN:** ZDI-CAN-14659
- **Date:** 2021-10-15
- **CVE:** CVE-2021-34976
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Foxit
- **Affected Products:** PDF Reader
- **Credit:** Milan Kyselica of IstroSec
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1207/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Foxit PDF Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of PDF files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxit.com/support/security-bulletins.html

## Disclosure Timeline

- 2021-08-18 - Vulnerability reported to vendor
- 2021-10-15 - Coordinated public release of advisory
