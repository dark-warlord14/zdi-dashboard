# ZDI-25-849: (Pwn2Own) NVIDIA Triton Inference Server SharedMemoryManager Error Message Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-849
- **ZDI-CAN:** ZDI-CAN-27181
- **Date:** 2025-08-20
- **CVE:** CVE-2025-23320
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** NVIDIA
- **Affected Products:** Triton Inference Server
- **Credit:** Ho Xuan Ninh (@izx) + Tri Dang (Sea Security)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-849/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of NVIDIA Triton Inference Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the SharedMemoryManager class. The issue results from outputting an error message that includes sensitive information. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

NVIDIA has issued an update to correct this vulnerability. More details can be found at: https://nvidia.custhelp.com/app/answers/detail/a_id/5687

## Disclosure Timeline

- 2025-06-03 - Vulnerability reported to vendor
- 2025-08-20 - Coordinated public release of advisory
- 2025-08-20 - Advisory Updated
