# ZDI-21-522: (0Day) Esri ArcReader PMF File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-522
- **ZDI-CAN:** ZDI-CAN-12580
- **Date:** 2021-05-06
- **CVE:** N/A
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Esri
- **Affected Products:** ArcReader
- **Credit:** Francis Provencher {PRL}
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-522/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Esri ArcReader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PMF files. Crafted data in an PMF file can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 12/04/20 – ZDI reported the vulnerability to the vendor 02/05/21 – The vendor requested technical clarification 02/09/20 – ZDI provided additional evidence 03/15/21 – The vendor indicated they had fixes ready 03/25/21 – The vendor communicated the cases would be included in a future release 03/25/21 – ZDI requested an ETA for the release and notified the vendor of the intention to publish the reports as 0-day advisories if no timely fix was provided 04/23/21 – ZDI requested an update and notified the vendor of the intention to publish the reports as 0-day advisories in 05/04/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-12-04 - Vulnerability reported to vendor
- 2021-05-06 - Coordinated public release of advisory
