# ZDI-26-275: Microsoft Qlib _mount_nfs_uri Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-275
- **ZDI-CAN:** ZDI-CAN-27212
- **Date:** 2026-04-15
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Qlib
- **Credit:** Peter Girnus (@gothburz) of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-275/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Microsoft Qlib. Authentication is not required to exploit this vulnerability. The specific flaw exists within the _mount_nfs_uri function. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fixed on May 31, 2025 https://msrc.microsoft.com/update-guide/acknowledgement/online

## Disclosure Timeline

- 2025-05-22 - Vulnerability reported to vendor
- 2026-04-15 - Coordinated public release of advisory
- 2026-04-15 - Advisory Updated
