# ZDI-25-830: (0Day) Schneider Electric EcoStruxure Power Monitoring Expert GetPagesAsImages Server-Side Request Forgery Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-830
- **ZDI-CAN:** ZDI-CAN-26463
- **Date:** 2025-08-12
- **CVE:** CVE-2025-54924
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Schneider Electric
- **Affected Products:** EcoStruxure Power Monitoring Expert
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-830/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Schneider Electric EcoStruxure Power Monitoring Expert. Authentication is not required to exploit this vulnerability. The specific flaw exists within the GetPagesAsImages method. The issue results from the lack of proper validation of a URI prior to accessing resources. An attacker can leverage this vulnerability to disclose information in the context of LOCAL SERVICE.

## Additional Details

04/16/25 – ZDI reported the vulnerability to ICS-CERT 04/17/25 – the vendor acknowledged the receipt of the report 05/13/25 – the vendor asked for technical details 05/23/25 - ZDI provided more evidence 07/15/25 – ZDI notified the vendor of the intention to publish the cases as a 0-day advisory -- Mitigation: Schneider Electric will include fixes for these vulnerabilities as part of the next release of the product PME 2024 R3, planned for November 11, 2025. Hotfix and Mitigation advice has been provided here: https://www.cisa.gov/news-events/ics-advisories/icsa-25-224-03 , https://download.schneider-electric.com/files?p_Doc_Ref=SEVD-2025-224-02&p_enDocType=Security+and+Safety+Notice&p_File_Name=SEVD-2025-224-02.pdf

## Disclosure Timeline

- 2025-04-16 - Vulnerability reported to vendor
- 2025-08-12 - Coordinated public release of advisory
- 2025-08-25 - Advisory Updated
