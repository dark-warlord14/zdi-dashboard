# ZDI-25-957: Oracle VirtualBox Virtio-net Uninitialized Memory Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-957
- **ZDI-CAN:** ZDI-CAN-27241
- **Date:** 2025-10-27
- **CVE:** CVE-2025-61759
- **CVSS:** 6.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Team Prison Break
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-957/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the Virtio-net device. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuoct2025.html

## Disclosure Timeline

- 2025-08-05 - Vulnerability reported to vendor
- 2025-10-27 - Coordinated public release of advisory
- 2025-10-27 - Advisory Updated
