# ZDI-23-1510: (0Day) D-Link D-View addDv7Probe XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1510
- **ZDI-CAN:** ZDI-CAN-19571
- **Date:** 2023-10-04
- **CVE:** CVE-2023-44412
- **CVSS:** 8.2
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:L
- **Affected Vendors:** D-Link
- **Affected Products:** D-View
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1510/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of D-Link D-View. Authentication is not required to exploit this vulnerability. The specific flaw exists within the addDv7Probe function. Due to the improper restriction of XML External Entity (XXE) references, a crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of SYSTEM.

## Additional Details

12/23/22 – The ZDI reported the vulnerability to the vendor. 08/25/23 – ZDI asked for an update. 08/30/23 – The vendor states they don’t have the case on record. 08/31/23 – ZDI forwarded the original report to the vendor. 09/29/23 – The ZDI informed the vendor that the case will be published as a zero-day advisory on 10/04/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2022-12-23 - Vulnerability reported to vendor
- 2023-10-04 - Coordinated public release of advisory
