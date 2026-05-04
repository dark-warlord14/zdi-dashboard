# ZDI-25-612: Hewlett Packard Enterprise AutoPass License Server Hard-coded Credentials Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-612
- **ZDI-CAN:** ZDI-CAN-25789
- **Date:** 2025-07-17
- **CVE:** CVE-2025-37105
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** AutoPass License Server
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-612/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Hewlett Packard Enterprise AutoPass License Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the hsqldb service, which listens on TCP port 9001 by default. The issue results from the use of hard-coded credentials. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://myenterpriselicense.hpe.com/cwp-ui/product-details/APLS/9.18/sw_free

## Disclosure Timeline

- 2024-12-05 - Vulnerability reported to vendor
- 2025-07-17 - Coordinated public release of advisory
- 2025-07-17 - Advisory Updated
