# ZDI-22-489: (0Day) Ecava IntegraXor Inkscape EMF File Parsing Uninitialized Pointer Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-489
- **ZDI-CAN:** ZDI-CAN-14384
- **Date:** 2022-03-09
- **CVE:** N/A
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Ecava
- **Affected Products:** IntegraXor
- **Credit:** Tran Van Khang - khangkito (VinCSS)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-489/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Ecava IntegraXor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of EMF files within the Inkscape component. The issue results from the lack of proper initialization of a pointer prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 07/13/21 – ZDI reported the vulnerabilities to ICS-CERT 07/16/21 – ICS-CERT acknowledged the reports 11/04/21 - ICS-CERT advised that the vulnerabilities affect a third-party component 11/10/21 – ICS-CERT requested technical clarification 11/14/21 – ZDI provided additional evidence 12/07/21 – ICS-CERT provided a draft of the advisory 12/24/21 – ZDI requested an update 01/09/22 – ZDI requested an update 01/10/22 – ICS-CERT communicated that the fix has not been published 03/01/22 – ZDI notified ICS-CERT of the intention to publish the cases as 0-day advisories on 03/09/22 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-07-13 - Vulnerability reported to vendor
- 2022-03-09 - Coordinated public release of advisory
- 2022-03-29 - Advisory Updated
