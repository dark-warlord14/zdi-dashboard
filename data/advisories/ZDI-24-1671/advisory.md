# ZDI-24-1671: GFI Archiver Telerik Web UI Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1671
- **ZDI-CAN:** ZDI-CAN-24041
- **Date:** 2024-12-11
- **CVE:** CVE-2024-11948
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** GFI
- **Affected Products:** Archiver
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1671/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of GFI Archiver. Authentication is not required to exploit this vulnerability. The specific flaw exists within the product installer. The issue results from the use of a vulnerable version of Telerik Web UI. An attacker can leverage this vulnerability to execute code in the context of NETWORK SERVICE.

## Additional Details

Fixed in version 15.7 - https://upgrade.gfi.com/check/gfi-archiver/12x

## Disclosure Timeline

- 2024-06-06 - Vulnerability reported to vendor
- 2024-12-11 - Coordinated public release of advisory
- 2024-12-11 - Advisory Updated
