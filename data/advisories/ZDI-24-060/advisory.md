# ZDI-24-060: Ivanti Avalanche WLAvalancheService TV_NL Null Pointer Dereference Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-060
- **ZDI-CAN:** ZDI-CAN-21992
- **Date:** 2024-01-11
- **CVE:** CVE-2023-46260
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** Monisc and phract
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-060/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Ivanti Avalanche. Authentication is not required to exploit this vulnerability. The specific flaw exists within the WLAvalancheService. The issue results from dereferencing a null pointer. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/Avalanche-6-4-2-Security-Hardening-and-CVEs-addressed?language=en_US

## Disclosure Timeline

- 2023-10-12 - Vulnerability reported to vendor
- 2024-01-11 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
