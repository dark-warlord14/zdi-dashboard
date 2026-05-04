# ZDI-20-1450: VMware Workstation SetGuestInfo Null Pointer Dereference Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1450
- **ZDI-CAN:** ZDI-CAN-11695
- **Date:** 2020-12-18
- **CVE:** CVE-2020-3999
- **CVSS:** 6.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:N/I:N/A:H
- **Affected Vendors:** VMware
- **Affected Products:** Workstation
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1450/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of VMware Workstation. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the implementation of the SetGuestInfo RPC function. The issue results from dereferencing a null pointer. An attacker can leverage this vulnerability to create a denial-of-service condition on the hypervisor.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2020-0029.html

## Disclosure Timeline

- 2020-08-14 - Vulnerability reported to vendor
- 2020-12-18 - Coordinated public release of advisory
