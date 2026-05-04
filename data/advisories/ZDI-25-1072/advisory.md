# ZDI-25-1072: IceWarp14 X-File-Operation Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1072
- **ZDI-CAN:** ZDI-CAN-27394
- **Date:** 2025-12-10
- **CVE:** CVE-2025-14500
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** IceWarp
- **Affected Products:** IceWarp
- **Credit:** Oscar Bataille
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1072/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of IceWarp. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the X-File-Operation header. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

IceWarp has issued an update to correct this vulnerability. More details can be found at: https://support.icewarp.com/hc/en-us/community/posts/40040980098705-EPOS-Update-2-build-9-14-2-0-9

## Disclosure Timeline

- 2025-09-26 - Vulnerability reported to vendor
- 2025-12-10 - Coordinated public release of advisory
- 2025-12-10 - Advisory Updated
