# ZDI-25-933: (Pwn2Own) Redis Lua Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-933
- **ZDI-CAN:** ZDI-CAN-27195
- **Date:** 2025-10-06
- **CVE:** CVE-2025-49844
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Redis
- **Affected Products:** Redis
- **Credit:** Benny Isaacs, Nir Brakha, Sagi Tzadik (@sagitz_)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-933/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Redis. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of certain string values by the embedded Lua interpreter. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Redis has issued an update to correct this vulnerability. More details can be found at: https://github.com/redis/redis/security/advisories/GHSA-4789-qfc9-5f9q

## Disclosure Timeline

- 2025-06-05 - Vulnerability reported to vendor
- 2025-10-06 - Coordinated public release of advisory
- 2025-10-06 - Advisory Updated
