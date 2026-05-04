# ZDI-26-061: NVIDIA Triton Inference Server EVBufferToJson Uncaught Exception Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-061
- **ZDI-CAN:** ZDI-CAN-26889
- **Date:** 2026-02-04
- **CVE:** CVE-2025-33201
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** NVIDIA
- **Affected Products:** Triton Inference Server
- **Credit:** Tyler Zars and Rob Blakely of the Technical Debt Collectors
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-061/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of NVIDIA Triton Inference Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the EVBufferToJson method. The issue results from the lack of proper validation of user-supplied data, which can result in an uncaught exception. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

NVIDIA has issued an update to correct this vulnerability. More details can be found at: https://nvidia.custhelp.com/app/answers/detail/a_id/5734

## Disclosure Timeline

- 2025-09-19 - Vulnerability reported to vendor
- 2026-02-04 - Coordinated public release of advisory
- 2026-02-04 - Advisory Updated
