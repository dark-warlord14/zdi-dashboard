# ZDI-25-598: Oracle VirtualBox BusLogic Uninitialized Memory Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-598
- **ZDI-CAN:** ZDI-CAN-26654
- **Date:** 2025-07-15
- **CVE:** CVE-2025-53025
- **CVSS:** 6.0
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Viettel Cyber Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-598/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the BusLogic module. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujul2025.html

## Disclosure Timeline

- 2025-05-23 - Vulnerability reported to vendor
- 2025-07-15 - Coordinated public release of advisory
- 2025-07-15 - Advisory Updated
