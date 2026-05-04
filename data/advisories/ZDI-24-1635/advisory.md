# ZDI-24-1635: Hewlett Packard Enterprise Insight Remote Support setInputStream XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1635
- **ZDI-CAN:** ZDI-CAN-24811
- **Date:** 2024-12-02
- **CVE:** CVE-2024-11622
- **CVSS:** 7.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Insight Remote Support
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1635/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Hewlett Packard Enterprise Insight Remote Support. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the setInputStream method. Due to the improper restriction of XML External Entity (XXE) references, a crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose files in the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbgn04731en_us&docLocale=en_US

## Disclosure Timeline

- 2024-09-19 - Vulnerability reported to vendor
- 2024-12-02 - Coordinated public release of advisory
- 2024-12-02 - Advisory Updated
