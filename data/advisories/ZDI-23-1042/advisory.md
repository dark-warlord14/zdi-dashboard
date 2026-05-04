# ZDI-23-1042: VBASE VISAM Automation Base FB.XML File Parsing XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1042
- **ZDI-CAN:** ZDI-CAN-19107
- **Date:** 2023-08-08
- **CVE:** CVE-2022-41696
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N
- **Affected Vendors:** VBASE
- **Affected Products:** VISAM Automation Base
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1042/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of VBASE VISAM Automation Base. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of FB.XML files. Due to the improper restriction of XML External Entity (XXE) references, a crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of the current process.

## Additional Details

VBASE has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-23-080-05

## Disclosure Timeline

- 2022-12-02 - Vulnerability reported to vendor
- 2023-08-08 - Coordinated public release of advisory
