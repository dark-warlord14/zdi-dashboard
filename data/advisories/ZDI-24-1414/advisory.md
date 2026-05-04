# ZDI-24-1414: Oracle VirtualBox BusLogic Uninitialized Memory Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1414
- **ZDI-CAN:** ZDI-CAN-25016
- **Date:** 2024-10-17
- **CVE:** CVE-2024-21273
- **CVSS:** 6.0
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** phudq from Viettel cyber security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1414/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the BusLogic module. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuoct2024verbose.html

## Disclosure Timeline

- 2024-09-19 - Vulnerability reported to vendor
- 2024-10-17 - Coordinated public release of advisory
- 2024-10-17 - Advisory Updated
