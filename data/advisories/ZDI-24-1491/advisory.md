# ZDI-24-1491: Ivanti Avalanche WLAvalancheService TV_FC Infinite Loop Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1491
- **ZDI-CAN:** ZDI-CAN-25454
- **Date:** 2024-11-13
- **CVE:** CVE-2024-50320
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** Alex Williams of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1491/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Ivanti Avalanche. Authentication is not required to exploit this vulnerability. The specific flaw exists within the WLAvalancheService service, which listens on TCP port 1777 by default. The issue results from a lack of a proper exit condition in a loop. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/Security-Advisory-Ivanti-Avalanche-Multiple-CVEs-Q4-2024-Release

## Disclosure Timeline

- 2024-10-08 - Vulnerability reported to vendor
- 2024-11-13 - Coordinated public release of advisory
- 2024-11-13 - Advisory Updated
