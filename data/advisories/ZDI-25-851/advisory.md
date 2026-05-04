# ZDI-25-851: (Pwn2Own) NVIDIA Triton Inference Server IPC Push Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-851
- **ZDI-CAN:** ZDI-CAN-27250
- **Date:** 2025-08-20
- **CVE:** CVE-2025-23318
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NVIDIA
- **Affected Products:** Triton Inference Server
- **Credit:** Ho Xuan Ninh (@izx) + Tri Dang (Sea Security)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-851/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of NVIDIA Triton Inference Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of IPC messages. A crafted IPC Push request can trigger a write past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of root.

## Additional Details

NVIDIA has issued an update to correct this vulnerability. More details can be found at: https://nvidia.custhelp.com/app/answers/detail/a_id/5687

## Disclosure Timeline

- 2025-06-27 - Vulnerability reported to vendor
- 2025-08-20 - Coordinated public release of advisory
- 2025-08-20 - Advisory Updated
