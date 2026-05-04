# ZDI-25-145: NVIDIA Riva Triton Inference Server Missing Authentication Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-145
- **ZDI-CAN:** ZDI-CAN-25794
- **Date:** 2025-03-13
- **CVE:** CVE-2025-23242
- **CVSS:** 7.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** NVIDIA
- **Affected Products:** Riva
- **Credit:** David Fiser and Alfredo Oliveira ( Nebula of Trend Micro )
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-145/
## Vulnerability Details

This vulnerability allows remote attackers to access protected functionality on affected installations of NVIDIA Riva. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of the Triton Inference Server. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to access the Triton Inference Server API on the target system.

## Additional Details

NVIDIA has issued an update to correct this vulnerability. More details can be found at: https://nvidia.custhelp.com/app/answers/detail/a_id/5625

## Disclosure Timeline

- 2024-11-15 - Vulnerability reported to vendor
- 2025-03-13 - Coordinated public release of advisory
- 2025-03-13 - Advisory Updated
