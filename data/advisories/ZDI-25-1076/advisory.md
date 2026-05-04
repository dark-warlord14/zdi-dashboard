# ZDI-25-1076: (0Day) pdfforge PDF Architect PDF File Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1076
- **ZDI-CAN:** ZDI-CAN-27902
- **Date:** 2025-12-11
- **CVE:** CVE-2025-14419
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** pdfforge
- **Affected Products:** PDF Architect
- **Credit:** Mat Powell of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1076/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of pdfforge PDF Architect. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PDF files. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

08/12/25 - ZDI reported the vulnerability to the vendor 09/24/25 - ZDI asked for updates 11/10/25 - ZDI asked for updates 12/05/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory on 12/11/25 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-08-12 - Vulnerability reported to vendor
- 2025-12-11 - Coordinated public release of advisory
- 2025-12-11 - Advisory Updated
