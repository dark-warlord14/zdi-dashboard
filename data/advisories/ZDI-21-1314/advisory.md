# ZDI-21-1314: Jenkins pom2config XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1314
- **ZDI-CAN:** ZDI-CAN-13947
- **Date:** 2021-11-16
- **CVE:** CVE-2021-43576
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Jenkins
- **Affected Products:** pom2config
- **Credit:** Adith Sudhakar
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1314/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Jenkins pom2config. Authentication is required to exploit this vulnerability. The specific flaw exists within the Pom2Config class. Due to the improper restriction of XML External Entity (XXE) references, a crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of the service account.

## Additional Details

Jenkins has issued an update to correct this vulnerability. More details can be found at: https://www.jenkins.io/security/advisory/2021-11-12/#SECURITY-2415

## Disclosure Timeline

- 2021-07-09 - Vulnerability reported to vendor
- 2021-11-16 - Coordinated public release of advisory
