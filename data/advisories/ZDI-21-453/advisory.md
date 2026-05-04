# ZDI-21-453: Oracle VirtualBox VRDP Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-453
- **ZDI-CAN:** ZDI-CAN-12407
- **Date:** 2021-04-22
- **CVE:** CVE-2021-2279
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** JungHyun Kim(@jidoc01) of VirtualBoBs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-453/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Oracle VirtualBox. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of drdynvc packets. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the RDP service.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2021.html

## Disclosure Timeline

- 2021-01-05 - Vulnerability reported to vendor
- 2021-04-22 - Coordinated public release of advisory
