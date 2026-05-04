# ZDI-25-1012: NVIDIA AIStore AuthN users Missing Authentication for Critical Function Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1012
- **ZDI-CAN:** ZDI-CAN-27857
- **Date:** 2025-11-14
- **CVE:** CVE-2025-33185
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** NVIDIA
- **Affected Products:** AIStore
- **Credit:** Peter Girnus (@gothburz) of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1012/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of NVIDIA AIStore. Authentication is not required to exploit this vulnerability. The specific flaw exists within the users endpoint. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to disclose stored user names, leading to further compromise.

## Additional Details

NVIDIA has issued an update to correct this vulnerability. More details can be found at: https://nvidia.custhelp.com/app/answers/detail/a_id/5724

## Disclosure Timeline

- 2025-08-12 - Vulnerability reported to vendor
- 2025-11-14 - Coordinated public release of advisory
- 2025-11-14 - Advisory Updated
