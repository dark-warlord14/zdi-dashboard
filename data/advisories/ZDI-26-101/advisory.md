# ZDI-26-101: Oracle VirtualBox BusLogic Uninitialized Memory Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-101
- **ZDI-CAN:** ZDI-CAN-28080
- **Date:** 2026-02-13
- **CVE:** CVE-2026-21963
- **CVSS:** 6.0
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Viettel Cyber Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-101/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the BusLogic module. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujan2026.html

## Disclosure Timeline

- 2025-10-09 - Vulnerability reported to vendor
- 2026-02-13 - Coordinated public release of advisory
- 2026-02-13 - Advisory Updated
