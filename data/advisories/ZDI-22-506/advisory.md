# ZDI-22-506: Cisco Nexus Dashboard Fabric Controller AMF Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-506
- **ZDI-CAN:** ZDI-CAN-14805
- **Date:** 2022-03-11
- **CVE:** CVE-2017-5641
- **CVSS:** 7.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Cisco
- **Affected Products:** Nexus Dashboard Fabric Controller
- **Credit:** Pedro Ribeiro (@pedrib1337 | pedrib@gmail.com) from Agile Information Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-506/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Cisco Nexus Dashboard Fabric Controller. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the AMF protocol. Crafted data in an AMF protocol message can trigger the deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the fmserver user.

## Additional Details

Fixed in version 11.5(4) or later

## Disclosure Timeline

- 2021-09-10 - Vulnerability reported to vendor
- 2022-03-11 - Coordinated public release of advisory
