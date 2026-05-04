# ZDI-25-1013: NVIDIA AIStore AuthN Hard-coded Credentials Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1013
- **ZDI-CAN:** ZDI-CAN-27858
- **Date:** 2025-11-14
- **CVE:** CVE-2025-33186
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NVIDIA
- **Affected Products:** AIStore
- **Credit:** Peter Girnus (@gothburz) of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1013/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of NVIDIA AIStore. Authentication is not required to exploit this vulnerability. The specific flaw exists within the AuthN authentication mechanism. The issue results from the use of hard-coded credentials. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

NVIDIA has issued an update to correct this vulnerability. More details can be found at: https://nvidia.custhelp.com/app/answers/detail/a_id/5724

## Disclosure Timeline

- 2025-08-12 - Vulnerability reported to vendor
- 2025-11-14 - Coordinated public release of advisory
- 2025-11-14 - Advisory Updated
