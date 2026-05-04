# ZDI-25-827: (0Day) Schneider Electric EcoStruxure Power Monitoring Expert GetTgmlContent Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-827
- **ZDI-CAN:** ZDI-CAN-26273
- **Date:** 2025-08-12
- **CVE:** CVE-2025-54926
- **CVSS:** 4.9
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Schneider Electric
- **Affected Products:** EcoStruxure Power Monitoring Expert
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-827/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Schneider Electric EcoStruxure Power Monitoring Expert. Authentication is required to exploit this vulnerability. The specific flaw exists within the GetTgmlContent method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of LOCAL SERVICE.

## Additional Details

04/02/25 – ZDI reported the vulnerability to ICS-CERT 04/04/25 – the vendor acknowledged the receipt of the report 05/13/25 – the vendor confirmed the reported behaviour 06/16/25 – the vendor communicated that the fix would be part of the November’s release 07/14/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Schneider Electric will include fixes for these vulnerabilities as part of the next release of the product PME 2024 R3, planned for November 11, 2025. Hotfix and Mitigation advice has been provided here: https://www.cisa.gov/news-events/ics-advisories/icsa-25-224-03 , https://download.schneider-electric.com/files?p_Doc_Ref=SEVD-2025-224-02&p_enDocType=Security+and+Safety+Notice&p_File_Name=SEVD-2025-224-02.pdf

## Disclosure Timeline

- 2025-04-02 - Vulnerability reported to vendor
- 2025-08-12 - Coordinated public release of advisory
- 2025-08-25 - Advisory Updated
