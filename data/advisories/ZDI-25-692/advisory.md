# ZDI-25-692: Oracle VirtualBox VirtIO-SCSI Uninitialized Memory Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-692
- **ZDI-CAN:** ZDI-CAN-25015
- **Date:** 2025-07-29
- **CVE:** CVE-2024-21273
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** phudq from Viettel cyber security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-692/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the VirtIO-SCSI module. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuoct2024verbose.html

## Disclosure Timeline

- 2024-10-08 - Vulnerability reported to vendor
- 2025-07-29 - Coordinated public release of advisory
- 2025-07-29 - Advisory Updated
