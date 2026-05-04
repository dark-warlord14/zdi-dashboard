# ZDI-24-1151: Ivanti Avalanche WLAvalancheService Null Pointer Dereference Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1151
- **ZDI-CAN:** ZDI-CAN-24220
- **Date:** 2024-08-15
- **CVE:** CVE-2024-37399
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** monisc and phract
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1151/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Ivanti Avalanche. Authentication is not required to exploit this vulnerability. The specific flaw exists within the WLAvalancheService service, which listens on TCP port 1777 by default. The issue results from dereferencing a null pointer. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/Security-Advisory-Ivanti-Avalanche-6-4-4-CVE-2024-38652-CVE-2024-38653-CVE-2024-36136-CVE-2024-37399-CVE-2024-37373?language=en_US

## Disclosure Timeline

- 2024-06-28 - Vulnerability reported to vendor
- 2024-08-15 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
