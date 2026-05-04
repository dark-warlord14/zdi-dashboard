# ZDI-24-1413: Oracle VirtualBox TPM Heap-based Buffer Overflow Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1413
- **ZDI-CAN:** ZDI-CAN-23961
- **Date:** 2024-10-17
- **CVE:** CVE-2024-21259
- **CVSS:** 7.5
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** YingMuo (@YingMuo), working with DEVCORE Internship Program
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1413/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the implementation of the virtual TPM device. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuoct2024verbose.html

## Disclosure Timeline

- 2024-07-30 - Vulnerability reported to vendor
- 2024-10-17 - Coordinated public release of advisory
- 2024-10-17 - Advisory Updated
