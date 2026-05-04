# ZDI-20-1284: WECON LeviStudioU XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1284
- **ZDI-CAN:** ZDI-CAN-10607
- **Date:** 2020-10-22
- **CVE:** CVE-2020-25186
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N
- **Affected Vendors:** WECON
- **Affected Products:** LeviStudioU
- **Credit:** Mehmet D. INCE @mdisec from T0.Group
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1284/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of WECON LeviStudioU. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of UMP files. Due to the improper restriction of XML External Entity (XXE) references, a specially crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of Administrator.

## Additional Details

WECON has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-20-238-03

## Disclosure Timeline

- 2020-05-26 - Vulnerability reported to vendor
- 2020-10-22 - Coordinated public release of advisory
