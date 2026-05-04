# ZDI-20-1215: Micro Focus Operations Bridge Reporter shrboadmin Use of Hard-coded Credentials Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1215
- **ZDI-CAN:** ZDI-CAN-11075
- **Date:** 2020-09-23
- **CVE:** CVE-2020-11857
- **CVSS:** 7.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Micro Focus
- **Affected Products:** Operations Bridge Reporter
- **Credit:** Pedro Ribeiro (pedrib@gmail.com|@pedrib1337) from Agile Information Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1215/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Micro Focus Operations Bridge Reporter. Authentication is not required to exploit this vulnerability. The specific flaw exists within the creation of the shrboadmin user during installation. The product contains a hard-coded password for this account. An attacker can leverage this vulnerability to execute arbitrary code in the context of the shrboadmin user.

## Additional Details

Micro Focus has issued an update to correct this vulnerability. More details can be found at: https://softwaresupport.softwaregrp.com/doc/KM03710590

## Disclosure Timeline

- 2020-06-10 - Vulnerability reported to vendor
- 2020-09-23 - Coordinated public release of advisory
