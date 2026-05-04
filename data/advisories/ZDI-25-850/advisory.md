# ZDI-25-850: (Pwn2Own) NVIDIA Triton Inference Server LoadFromSharedMemory Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-850
- **ZDI-CAN:** ZDI-CAN-27249
- **Date:** 2025-08-20
- **CVE:** CVE-2025-23333
- **CVSS:** 5.9
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** NVIDIA
- **Affected Products:** Triton Inference Server
- **Credit:** Ho Xuan Ninh (@izx) + Tri Dang (Sea Security)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-850/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of NVIDIA Triton Inference Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the LoadFromSharedMemory function. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated data structure. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

NVIDIA has issued an update to correct this vulnerability. More details can be found at: https://nvidia.custhelp.com/app/answers/detail/a_id/5687

## Disclosure Timeline

- 2025-07-08 - Vulnerability reported to vendor
- 2025-08-20 - Coordinated public release of advisory
- 2025-08-20 - Advisory Updated
