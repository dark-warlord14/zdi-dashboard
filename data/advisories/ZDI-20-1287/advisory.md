# ZDI-20-1287: Micro Focus Operations Bridge Manager diagnostics Use of Hard-coded Credentials Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1287
- **ZDI-CAN:** ZDI-CAN-11201
- **Date:** 2020-10-28
- **CVE:** CVE-2020-11854
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Micro Focus
- **Affected Products:** Operations Bridge Manager
- **Credit:** Pedro Ribeiro (pedrib@gmail.com | @pedrib1337) from Agile Information Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1287/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Micro Focus Operations Bridge Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the product's authentication mechanism. The product contains a hard-coded password for the diagnostics user account. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Micro Focus has issued an update to correct this vulnerability. More details can be found at: https://softwaresupport.softwaregrp.com/doc/KM03747658

## Disclosure Timeline

- 2020-06-19 - Vulnerability reported to vendor
- 2020-10-28 - Coordinated public release of advisory
