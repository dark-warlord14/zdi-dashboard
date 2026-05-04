# ZDI-22-1446: Oracle VirtualBox VRDP Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1446
- **ZDI-CAN:** ZDI-CAN-17683
- **Date:** 2022-10-21
- **CVE:** CVE-2022-39424
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** kn32
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1446/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Oracle VirtualBox. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of smartcard I/O messages. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the RDP service.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuoct2022.html

## Disclosure Timeline

- 2022-09-06 - Vulnerability reported to vendor
- 2022-10-21 - Coordinated public release of advisory
