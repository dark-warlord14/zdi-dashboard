# ZDI-20-130: Oracle VirtualBox VBoxVHWAHandleTable Out-Of-Bounds Access Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-130
- **ZDI-CAN:** ZDI-CAN-9389
- **Date:** 2020-01-15
- **CVE:** CVE-2020-2682
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** anhdaden of StarLabs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-130/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the VBoxVHWAHandleTable class. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated array. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujan2020.html

## Disclosure Timeline

- 2019-10-31 - Vulnerability reported to vendor
- 2020-01-15 - Coordinated public release of advisory
