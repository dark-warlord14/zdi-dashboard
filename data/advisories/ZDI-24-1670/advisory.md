# ZDI-24-1670: GFI Archiver Core Service Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1670
- **ZDI-CAN:** ZDI-CAN-24029
- **Date:** 2024-12-11
- **CVE:** CVE-2024-11947
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** GFI
- **Affected Products:** Archiver
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1670/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of GFI Archiver. Authentication is required to exploit this vulnerability. The specific flaw exists within the Core Service, which listens on TCP port 8017 by default. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Fixed in version 15.7 - https://upgrade.gfi.com/check/gfi-archiver/12x

## Disclosure Timeline

- 2024-06-06 - Vulnerability reported to vendor
- 2024-12-11 - Coordinated public release of advisory
- 2024-12-11 - Advisory Updated
