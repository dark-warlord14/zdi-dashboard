# ZDI-24-411: (Pwn2Own) Oracle VirtualBox BusLogic Uninitialized Memory Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-411
- **ZDI-CAN:** ZDI-CAN-23798
- **Date:** 2024-04-26
- **CVE:** CVE-2024-21121
- **CVSS:** 6.0
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Corentin "@OnlyTheDuck" BAYET from REverse Tactics
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-411/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the BusLogic module. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2024.html

## Disclosure Timeline

- 2024-03-28 - Vulnerability reported to vendor
- 2024-04-26 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
