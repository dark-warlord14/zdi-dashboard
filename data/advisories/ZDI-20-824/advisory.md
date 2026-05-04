# ZDI-20-824: (0Day) (Pwn2Own) Rockwell Automation Studio 5000 AML File Parsing XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-824
- **ZDI-CAN:** ZDI-CAN-10290
- **Date:** 2020-07-09
- **CVE:** CVE-2020-12025
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Rockwell Automation
- **Affected Products:** Studio 5000
- **Credit:** Chris Anastasio (muffin) and Steven Seeley (mr_me) of Incite Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-824/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Rockwell Automation Studio 5000. Authentication is not required to exploit this vulnerability. The specific flaw exists within the parsing of AML files. Due to the improper restriction of XML External Entity (XXE) references, a specially crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 01/22/20 – ZDI disclosed the report to the vendor onsite at Pwn2Own at S4 01/30/20 – The vendor requested an extension and ZDI offered a 10-day extension 04/29/20 – ZDI requested an update 04/30/20 – ZDI provided an additional extension (due to Covid-19 quarantine) 06/02/20 – All parties agreed to provide the materials to ICS-CERT 06/02/20 – The vendor advised ZDI the advisory release would be 06/26/20 06/26/20 – The vendor advised ZDI they would miss the date and ZDI agreed to coordinate a 0-day advisory -- Mitigation: Rockwell's recommendation: Rockwell Automation customers using AML or RDF files should not accept files from unknown sources and remain cautious of social engineering attempts that may take advantage of this vulnerability

## Disclosure Timeline

- 2020-01-30 - Vulnerability reported to vendor
- 2020-07-09 - Coordinated public release of advisory
- 2021-06-29 - Advisory Updated
