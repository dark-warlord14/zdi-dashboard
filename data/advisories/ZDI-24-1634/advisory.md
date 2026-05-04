# ZDI-24-1634: Hewlett Packard Enterprise AutoPass License Server XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1634
- **ZDI-CAN:** ZDI-CAN-24694
- **Date:** 2024-12-02
- **CVE:** CVE-2024-51770
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** AutoPass License Server
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1634/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Hewlett Packard Enterprise AutoPass License Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the web service, which listens on TCP port 5814 by default. Due to the improper restriction of XML External Entity (XXE) references, a crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbgn04760en_us&docLocale=en_US

## Disclosure Timeline

- 2024-07-24 - Vulnerability reported to vendor
- 2024-12-02 - Coordinated public release of advisory
- 2024-12-02 - Advisory Updated
