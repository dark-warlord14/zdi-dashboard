# ZDI-23-982: Oracle VirtualBox VRDP Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-982
- **ZDI-CAN:** ZDI-CAN-21259
- **Date:** 2023-07-26
- **CVE:** CVE-2023-22018
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** kn32
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-982/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Oracle VirtualBox. Authentication may or may not be required to exploit this vulnerability, depending upon product configuration. The specific flaw exists within the handling of USB request messages. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the RDP service.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujul2023.html

## Disclosure Timeline

- 2023-06-21 - Vulnerability reported to vendor
- 2023-07-26 - Coordinated public release of advisory
