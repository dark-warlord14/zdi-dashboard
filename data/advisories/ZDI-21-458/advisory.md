# ZDI-21-458: Oracle OSS Support Tools Diagnostic Assistant XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-458
- **ZDI-CAN:** ZDI-CAN-12564
- **Date:** 2021-04-22
- **CVE:** CVE-2021-2303
- **CVSS:** 4.9
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** OSS Support Tools
- **Credit:** Quynh Le of VNPT ISC
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-458/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Oracle OSS Support Tools. Authentication is required to exploit this vulnerability. The specific flaw exists within the Diagnostic Assistant component. Due to the improper restriction of XML External Entity (XXE) references, a crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of the service account.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2021.html

## Disclosure Timeline

- 2021-01-22 - Vulnerability reported to vendor
- 2021-04-22 - Coordinated public release of advisory
