# ZDI-21-266: Siemens Solid Edge Viewer SEECTCXML File Parsing XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-266
- **ZDI-CAN:** ZDI-CAN-11923
- **Date:** 2021-03-11
- **CVE:** CVE-2020-28387
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N
- **Affected Vendors:** Siemens
- **Affected Products:** Solid Edge Viewer
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-266/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Siemens Solid Edge Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SEECTCXML files. Due to the improper restriction of XML External Entity (XXE) references, a crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of the current process.

## Additional Details

Siemens has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-068-09

## Disclosure Timeline

- 2020-11-11 - Vulnerability reported to vendor
- 2021-03-11 - Coordinated public release of advisory
