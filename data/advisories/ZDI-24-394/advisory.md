# ZDI-24-394: Ivanti Avalanche WLAvalancheService Null Pointer Dereference Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-394
- **ZDI-CAN:** ZDI-CAN-22990
- **Date:** 2024-04-23
- **CVE:** CVE-2024-27978
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-394/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Ivanti Avalanche. Authentication is required to exploit this vulnerability. The specific flaw exists within the WLAvalancheService, which listens on TCP port 1777 by default. The issue results from dereferencing a null pointer. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/Avalanche-6-4-3-Security-Hardening-and-CVEs-addressed?language=en_US

## Disclosure Timeline

- 2024-01-09 - Vulnerability reported to vendor
- 2024-04-23 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
