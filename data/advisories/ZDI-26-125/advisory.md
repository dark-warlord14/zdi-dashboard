# ZDI-26-125: Docker Desktop grpcfuse Kernel Module Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-125
- **ZDI-CAN:** ZDI-CAN-28631
- **Date:** 2026-02-25
- **CVE:** CVE-2026-2664
- **CVSS:** 6.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Docker
- **Affected Products:** Desktop
- **Credit:** Pumpkin (@u1f383) from DEVCORE Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-125/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Docker Desktop. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of procfs arguments. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilties to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Docker has issued an update to correct this vulnerability. More details can be found at: https://docs.docker.com/desktop/release-notes/#4620

## Disclosure Timeline

- 2025-12-18 - Vulnerability reported to vendor
- 2026-02-25 - Coordinated public release of advisory
- 2026-02-25 - Advisory Updated
