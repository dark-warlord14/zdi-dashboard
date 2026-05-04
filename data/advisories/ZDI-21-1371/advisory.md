# ZDI-21-1371: (0Day) Esri ArcReader PMF File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1371
- **ZDI-CAN:** ZDI-CAN-14437
- **Date:** 2021-11-30
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Esri
- **Affected Products:** ArcReader
- **Credit:** Tran Van Khang - khangkito (VinCSS)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1371/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Esri ArcReader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PMF files. Crafted data in a PMF file can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 07/13/21 – ZDI reported the vulnerability to the vendor 07/20/21 – The vendor acknowledged the report 11/01/21 – The vendor requested one month extension 11/05/21 – ZDI agreed to provide 10 days extension only 11/19/21 – ZDI notified the vendor of the intention to publish the report as 0-day advisory on 11/26/21 11/24/21 – The vendor sent a publication that clarifis that the product is being deprecated and that customers should shift to current (non-legacy) products. 11/26/21 – ZDI informed the vendor of the intention to publish the report as 0-day advisory on 11/30/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-07-13 - Vulnerability reported to vendor
- 2021-11-30 - Coordinated public release of advisory
