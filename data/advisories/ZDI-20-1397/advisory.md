# ZDI-20-1397: Arcserve D2D getNews XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1397
- **ZDI-CAN:** ZDI-CAN-11103
- **Date:** 2020-12-04
- **CVE:** CVE-2020-27858
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Arcserve
- **Affected Products:** D2D
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1397/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of CA Arcserve D2D. Authentication is not required to exploit this vulnerability. The specific flaw exists within the getNews method. Due to the improper restriction of XML External Entity (XXE) references, a specially-crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of SYSTEM.

## Additional Details

Arcserve has issued an update to correct this vulnerability. More details can be found at: https://support.arcserve.com/s/article/P00002159?

## Disclosure Timeline

- 2020-06-05 - Vulnerability reported to vendor
- 2020-12-04 - Coordinated public release of advisory
