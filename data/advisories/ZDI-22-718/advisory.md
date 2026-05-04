# ZDI-22-718: (0Day) Rockwell Automation ISaGRAF isasln File Parsing XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-718
- **ZDI-CAN:** ZDI-CAN-15178
- **Date:** 2022-05-09
- **CVE:** N/A
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N
- **Affected Vendors:** Rockwell Automation
- **Affected Products:** ISaGRAF
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-718/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Rockwell Automation ISaGRAF. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of isasln files. Due to the improper restriction of XML External Entity (XXE) references, a crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 11/18/21 – ZDI reported the vulnerability to ICS-CERT 11/18/21 – ICS-CERT acknowledged the report 01/14/22 – ICS-CERT requested an extension until 03/31/2022 01/27/22 – ZDI provided an extension until 03/31/2022 03/23/22 – ZDI requested an update 04/12/22 – ICS-CERT communicated that the case has not been fixed 04/14/22 – ZDI notified ICS-CERT of the intention to publish the case as 0-day advisory on 04/21/22 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-11-18 - Vulnerability reported to vendor
- 2022-05-09 - Coordinated public release of advisory
- 2022-05-10 - Advisory Updated
