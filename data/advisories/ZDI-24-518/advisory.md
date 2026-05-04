# ZDI-24-518: Progress Software Telerik Reporting ValidateMetadaUri XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-518
- **ZDI-CAN:** ZDI-CAN-23880
- **Date:** 2024-05-29
- **CVE:** CVE-2024-4357
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Progress Software
- **Affected Products:** Telerik Reporting
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-518/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Progress Software Telerik Reporting. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the implementation of ValidateMetadaUri method. Due to the improper restriction of XML External Entity (XXE) references, a crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of SYSTEM.

## Additional Details

Progress Software has issued an update to correct this vulnerability. More details can be found at: https://docs.telerik.com/report-server/knowledge-base/xxe-vulnerability-cve-2024-4357

## Disclosure Timeline

- 2024-04-24 - Vulnerability reported to vendor
- 2024-05-29 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
