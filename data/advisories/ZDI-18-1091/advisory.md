# ZDI-18-1091: (0Day) Wecon LeviStudioU xmlparser LoadXMLFile XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1091
- **ZDI-CAN:** ZDI-CAN-6251
- **Date:** 2018-09-26
- **CVE:** CVE-2018-10614
- **CVSS:** 7.1
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Wecon
- **Affected Products:** LeviStudioU
- **Credit:** Jose Luis Zayas Banderas
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1091/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Wecon LeviStudioU. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of project files. Due to the improper restriction of XML External Entity (XXE) references, a specially crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information under the context of Administrator.

## Additional Details

Wecon has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-212-03 This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 05/18/18 - ZDI disclosed the reports to ICS-CERT 07/06/18 - ZDI inquired about the status of the reports 09/19/18 - ZDI notified ICS-CERT of the intent to 0-day these on 9/26 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2018-05-18 - Vulnerability reported to vendor
- 2018-09-26 - Coordinated public release of advisory
- 2018-09-26 - Advisory Updated
