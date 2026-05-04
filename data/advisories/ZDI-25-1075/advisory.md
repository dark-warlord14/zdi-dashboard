# ZDI-25-1075: (0Day) pdfforge PDF Architect XLS File Insufficient UI Warning Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1075
- **ZDI-CAN:** ZDI-CAN-27502
- **Date:** 2025-12-11
- **CVE:** CVE-2025-14418
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** pdfforge
- **Affected Products:** PDF Architect
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1075/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of pdfforge PDF Architect. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of XLS files. The issue results from allowing the execution of dangerous script without user warning. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

07/10/25 - ZDI reported the vulnerability to the vendor 07/17/25 – the vendor acknowledged the receipt of the report 09/24/25 - ZDI asked for updates 11/10/25 - ZDI asked for updates 12/05/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory on 12/11/25 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-07-10 - Vulnerability reported to vendor
- 2025-12-11 - Coordinated public release of advisory
- 2025-12-11 - Advisory Updated
