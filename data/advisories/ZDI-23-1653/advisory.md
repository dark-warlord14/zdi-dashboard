# ZDI-23-1653: Adobe RoboHelp Server UpdateCommandStream XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1653
- **ZDI-CAN:** ZDI-CAN-21305
- **Date:** 2023-11-15
- **CVE:** CVE-2023-22274
- **CVSS:** 8.2
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:L
- **Affected Vendors:** Adobe
- **Affected Products:** RoboHelp Server
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1653/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe RoboHelp Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the UpdateCommandStream method. Due to the improper restriction of XML External Entity (XXE) references, a crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of LOCAL SERVICE.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/robohelp-server/apsb23-53.html

## Disclosure Timeline

- 2023-07-13 - Vulnerability reported to vendor
- 2023-11-15 - Coordinated public release of advisory
