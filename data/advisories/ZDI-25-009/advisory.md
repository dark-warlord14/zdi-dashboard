# ZDI-25-009: Redis Stack RedisBloom Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-009
- **ZDI-CAN:** ZDI-CAN-24143
- **Date:** 2025-01-09
- **CVE:** CVE-2024-55656
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Redis
- **Affected Products:** Redis Stack
- **Credit:** Ricardo Silva (@rick2600) and Gabriel Quadros (@gqsilva)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-009/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Redis Stack. Authentication is required to exploit this vulnerability. The specific flaw exists within the RedisBloom module. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Redis has issued an update to correct this vulnerability. More details can be found at: https://redis.io/blog/security-advisory-cve-2024-46981-cve-2024-51737-cve-2024-51480-cve-2024-55656/

## Disclosure Timeline

- 2024-07-18 - Vulnerability reported to vendor
- 2025-01-09 - Coordinated public release of advisory
- 2025-01-09 - Advisory Updated
