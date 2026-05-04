# ZDI-26-019: Cisco Identity Services Engine getSpecificPLRfromAuthCode XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-019
- **ZDI-CAN:** ZDI-CAN-27889
- **Date:** 2026-01-09
- **CVE:** CVE-2026-20029
- **CVSS:** 4.9
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Cisco
- **Affected Products:** Identity Services Engine
- **Credit:** Bobby Gould (@bobbygould5) of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-019/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Cisco Identity Services Engine. Authentication is required to exploit this vulnerability. The specific flaw exists within the implementation of the getSpecificPLRfromAuthCode method. Due to the improper restriction of XML External Entity (XXE) references, a crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of the application.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-xxe-jWSbSDKt

## Disclosure Timeline

- 2025-08-14 - Vulnerability reported to vendor
- 2026-01-09 - Coordinated public release of advisory
- 2026-01-09 - Advisory Updated
