# ZDI-25-1044: NVIDIA Isaac-GR00T secure_server Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1044
- **ZDI-CAN:** ZDI-CAN-27954
- **Date:** 2025-12-09
- **CVE:** CVE-2025-33184
- **CVSS:** 7.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** NVIDIA
- **Affected Products:** Isaac-GR00T
- **Credit:** Peter Girnus (@gothburz) of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1044/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of NVIDIA Isaac-GR00T. Authentication is not required to exploit this vulnerability. The specific flaw exists within the secure_server method. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

NVIDIA has issued an update to correct this vulnerability. More details can be found at: https://nvidia.custhelp.com/app/answers/detail/a_id/5725

## Disclosure Timeline

- 2025-08-21 - Vulnerability reported to vendor
- 2025-12-09 - Coordinated public release of advisory
- 2025-12-09 - Advisory Updated
