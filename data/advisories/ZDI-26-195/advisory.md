# ZDI-26-195: (Pwn2Own) ChargePoint Home Flex Inclusion of Sensitive Information in Source Code Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-195
- **ZDI-CAN:** ZDI-CAN-26340
- **Date:** 2026-03-16
- **CVE:** CVE-2026-4155
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** ChargePoint
- **Affected Products:** Home Flex
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-195/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of ChargePoint Home Flex charging stations. Authentication is not required to exploit this vulnerability. The specific flaw exists within the genpw script. The issue results from the inclusion of a secret cryptographic seed value within the script. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Fixed in CPH50 firmware version 5.5.4.22

## Disclosure Timeline

- 2025-03-13 - Vulnerability reported to vendor
- 2026-03-16 - Coordinated public release of advisory
- 2026-03-16 - Advisory Updated
