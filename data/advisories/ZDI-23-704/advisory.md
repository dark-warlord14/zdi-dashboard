# ZDI-23-704: Linux Kernel ksmbd Session User Object Race Condition Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-704
- **ZDI-CAN:** ZDI-CAN-20595
- **Date:** 2023-05-17
- **CVE:** CVE-2023-32256
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:C/C:L/I:N/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Quentin Minster (@thalium_team)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-704/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Linux Kernel. Authentication is not required to exploit this vulnerability, but only systems with ksmbd enabled are vulnerable. The specific flaw exists within the processing of SMB2_QUERY_INFO and SMB2_LOGOFF commands. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://github.com/torvalds/linux/commit/abcc506a9a71976a8b4c9bf3ee6efd13229c1e19

## Disclosure Timeline

- 2023-05-01 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
