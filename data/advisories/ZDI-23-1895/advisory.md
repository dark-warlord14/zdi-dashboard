# ZDI-23-1895: (0Day) Voltronic Power ViewPower Pro doDocument XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1895
- **ZDI-CAN:** ZDI-CAN-22081
- **Date:** 2023-12-20
- **CVE:** CVE-2023-51591
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:L
- **Affected Vendors:** Voltronic Power
- **Affected Products:** ViewPower Pro
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1895/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Voltronic Power ViewPower Pro. Authentication is not required to exploit this vulnerability. The specific flaw exists within the doDocument method. Due to the improper restriction of XML External Entity (XXE) references, a crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of LOCAL SERVICE.

## Additional Details

08/03/23 – ZDI made multiple attempts to contact the vendor across sales, support, and professional networking channels, which yielded no response from the vendor. We also contacted CISA, who was unsuccessful in receiving a response from the vendor. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-11-17 - Vulnerability reported to vendor
- 2023-12-20 - Coordinated public release of advisory
