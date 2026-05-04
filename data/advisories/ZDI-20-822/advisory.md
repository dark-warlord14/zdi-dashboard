# ZDI-20-822: Veeam ONE Reporter_ImportLicense Page_Load XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-822
- **ZDI-CAN:** ZDI-CAN-10710
- **Date:** 2020-07-08
- **CVE:** CVE-2020-15419
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Veeam
- **Affected Products:** ONE
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-822/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Veeam ONE. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Reporter_ImportLicense class. Due to the improper restriction of XML External Entity (XXE) references, a specially crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose file contents in the context of SYSTEM.

## Additional Details

Veeam has issued an update to correct this vulnerability. More details can be found at: https://www.veeam.com/kb3221

## Disclosure Timeline

- 2020-05-14 - Vulnerability reported to vendor
- 2020-07-08 - Coordinated public release of advisory
