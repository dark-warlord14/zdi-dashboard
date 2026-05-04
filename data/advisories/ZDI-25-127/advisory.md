# ZDI-25-127: (0Day) (Pwn2Own) Samsung SmartThings Improper Verification of Cryptographic Signature Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-127
- **ZDI-CAN:** ZDI-CAN-25615
- **Date:** 2025-03-11
- **CVE:** CVE-2025-2233
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Samsung
- **Affected Products:** SmartThings
- **Credit:** NiNi (@terrynini38514) from DEVCORE Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-127/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of Samsung SmartThings. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Hub Local API service, which listens on TCP port 8766 by default. The issue results from the lack of proper verification of a cryptographic signature. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Fixed in version 0.55.5

## Disclosure Timeline

- 2024-10-31 - Vulnerability reported to vendor
- 2025-03-11 - Coordinated public release of advisory
- 2025-04-16 - Advisory Updated
