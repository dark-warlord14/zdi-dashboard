# ZDI-23-1622: NI DIAdem GPX File Parsing XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1622
- **ZDI-CAN:** ZDI-CAN-21871
- **Date:** 2023-11-14
- **CVE:** CVE-2023-5136
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N
- **Affected Vendors:** NI
- **Affected Products:** DIAdem
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1622/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of NI DIAdem. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of GPX files. Due to the improper restriction of XML External Entity (XXE) references, a crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of the current process.

## Additional Details

NI has issued an update to correct this vulnerability. More details can be found at: https://www.ni.com/en/support/documentation/supplemental/23/incorrect-permission-assignment-in-the-topografix-dataplug-for-gpx.html

## Disclosure Timeline

- 2023-09-13 - Vulnerability reported to vendor
- 2023-11-14 - Coordinated public release of advisory
