# ZDI-23-706: Linux Kernel ksmbd Session Race Condition Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-706
- **ZDI-CAN:** ZDI-CAN-20796
- **Date:** 2023-05-17
- **CVE:** CVE-2023-32258
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** TBD
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-706/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Linux Kernel. Authentication is not required to exploit this vulnerability, but only systems with ksmbd enabled are vulnerable. The specific flaw exists within the processing of SMB2_LOGOFF and SMB2_CLOSE commands. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to execute code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://github.com/torvalds/linux/commit/abcc506a9a71976a8b4c9bf3ee6efd13229c1e19

## Disclosure Timeline

- 2023-04-27 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
