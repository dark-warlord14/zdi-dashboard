# ZDI-25-1078: (0Day) pdfforge PDF Architect PDF File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1078
- **ZDI-CAN:** ZDI-CAN-27915
- **Date:** 2025-12-11
- **CVE:** CVE-2025-14421
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** pdfforge
- **Affected Products:** PDF Architect
- **Credit:** Mat Powell of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1078/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of pdfforge PDF Architect. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PDF files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

08/21/25 - ZDI reported the vulnerability to the vendor 09/24/25 - ZDI asked for updates 11/10/25 - ZDI asked for updates 12/05/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory on 12/11/25 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-08-21 - Vulnerability reported to vendor
- 2025-12-11 - Coordinated public release of advisory
- 2025-12-11 - Advisory Updated
