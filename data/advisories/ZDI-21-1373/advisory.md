# ZDI-21-1373: Jenkins Report Info XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1373
- **ZDI-CAN:** ZDI-CAN-13946
- **Date:** 2021-12-02
- **CVE:** N/A
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Jenkins
- **Affected Products:** Report Info
- **Credit:** Adith Sudhakar
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1373/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Jenkins Report Info. Authentication is required to exploit this vulnerability. The specific flaw exists within the PMD class. Due to the improper restriction of XML External Entity (XXE) references, a crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of the service account.

## Additional Details

Fixed in version 1.1

## Disclosure Timeline

- 2021-07-09 - Vulnerability reported to vendor
- 2021-12-02 - Coordinated public release of advisory
