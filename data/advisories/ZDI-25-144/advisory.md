# ZDI-25-144: NVIDIA Riva gRPC API Missing Authentication for Critical Function Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-144
- **ZDI-CAN:** ZDI-CAN-25682
- **Date:** 2025-03-13
- **CVE:** CVE-2025-23243
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:L
- **Affected Vendors:** NVIDIA
- **Affected Products:** Riva
- **Credit:** David Fiser and Alfredo Oliveira ( Nebula of Trend Micro )
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-144/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of NVIDIA Riva. Authentication is not required to exploit this vulnerability. The specific flaw exists within the riva_quickstart component. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

NVIDIA has issued an update to correct this vulnerability. More details can be found at: https://nvidia.custhelp.com/app/answers/detail/a_id/5625

## Disclosure Timeline

- 2024-11-05 - Vulnerability reported to vendor
- 2025-03-13 - Coordinated public release of advisory
- 2025-03-13 - Advisory Updated
