# ZDI-22-599: Bentley View 3DS File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-599
- **ZDI-CAN:** ZDI-CAN-16307
- **Date:** 2022-04-12
- **CVE:** CVE-2022-28308
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Bentley
- **Affected Products:** View
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-599/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Bentley View. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of 3DS files. Crafted data in a 3DS file can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Bentley has issued an update to correct this vulnerability. More details can be found at: https://www.bentley.com/en/common-vulnerability-exposure/be-2022-0003

## Disclosure Timeline

- 2022-01-21 - Vulnerability reported to vendor
- 2022-04-12 - Coordinated public release of advisory
