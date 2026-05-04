# ZDI-25-1082: (0Day) Soda PDF Desktop PDF File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1082
- **ZDI-CAN:** ZDI-CAN-27120
- **Date:** 2025-12-11
- **CVE:** CVE-2025-14409
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Soda PDF
- **Affected Products:** Desktop
- **Credit:** Rocco Calvi (@TecR0c) with TecSecurity
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1082/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Soda PDF Desktop. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PDF files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

06/19/25 - ZDI reported the vulnerability to Avanquest’s support team 07/01/25 – the vendor acknowledged the receipt of the report 08/11/25 - ZDI asked for updates 08/12/25 – the vendor acknowledged that the report was escalated to the proper department 11/10/25 - ZDI asked for updates 11/21/25 – the vendor indicated that they don't offer bounties or rewards 11/21/25 - ZDI confirmed not accepting any rewards or bounties and asked for the expected fix date 12/04/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory on 12/11/25 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-06-19 - Vulnerability reported to vendor
- 2025-12-11 - Coordinated public release of advisory
- 2025-12-11 - Advisory Updated
