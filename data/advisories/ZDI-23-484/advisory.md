# ZDI-23-484: (Pwn2Own) Oracle VirtualBox OHCI USB Controller Uninitialized Memory Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-484
- **ZDI-CAN:** ZDI-CAN-20670
- **Date:** 2023-04-24
- **CVE:** CVE-2023-21989
- **CVSS:** 6.0
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** dungdm(@_piers2) of Viettel Cyber Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-484/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the OHCI USB controller. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2023.html

## Disclosure Timeline

- 2023-03-30 - Vulnerability reported to vendor
- 2023-04-24 - Coordinated public release of advisory
