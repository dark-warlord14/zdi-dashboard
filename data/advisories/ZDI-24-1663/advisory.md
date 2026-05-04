# ZDI-24-1663: Veritas Enterprise Vault Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1663
- **ZDI-CAN:** ZDI-CAN-24405
- **Date:** 2024-12-11
- **CVE:** CVE-2024-53915
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Veritas
- **Affected Products:** Enterprise Vault
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1663/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Veritas Enterprise Vault. Authentication is required to exploit this vulnerability. The specific flaw exists within the EVFileSvrArcMngr service. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Veritas has issued an update to correct this vulnerability. More details can be found at: https://www.veritas.com/support/en_US/security/VTS24-014

## Disclosure Timeline

- 2024-07-24 - Vulnerability reported to vendor
- 2024-12-11 - Coordinated public release of advisory
- 2024-12-11 - Advisory Updated
