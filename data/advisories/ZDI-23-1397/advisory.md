# ZDI-23-1397: Visualware MyConnection Server doIForward XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1397
- **ZDI-CAN:** ZDI-CAN-21774
- **Date:** 2023-09-08
- **CVE:** CVE-2023-42035
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:L
- **Affected Vendors:** Visualware
- **Affected Products:** MyConnection Server
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1397/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Visualware MyConnection Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the doIForward method. Due to the improper restriction of XML External Entity (XXE) references, a crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of root.

## Additional Details

Visualware has issued an update to correct this vulnerability. More details can be found at: https://myconnectionserver.visualware.com/support/security-advisories

## Disclosure Timeline

- 2023-07-31 - Vulnerability reported to vendor
- 2023-09-08 - Coordinated public release of advisory
