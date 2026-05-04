# ZDI-19-944: Advantech WISE-PaaS/RMM RecoveryMgmt ActionCommd_ota XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-944
- **ZDI-CAN:** ZDI-CAN-9094
- **Date:** 2019-11-01
- **CVE:** CVE-2019-18227
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Advantech
- **Affected Products:** WISE-PaaS/RMM
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-944/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Advantech WISE-PasS/RMM. Authentication is not required to exploit this vulnerability. The specific flaw exists within the RecoveryMgmt class. Due to the improper restriction of XML External Entity (XXE) references, a specially crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of SYSTEM.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-19-304-01

## Disclosure Timeline

- 2019-08-20 - Vulnerability reported to vendor
- 2019-11-01 - Coordinated public release of advisory
