# ZDI-18-1242: VMware Workstation SVGA Heap-based Buffer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1242
- **ZDI-CAN:** ZDI-CAN-6365
- **Date:** 2018-10-16
- **CVE:** CVE-2018-6974
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** VMware
- **Affected Products:** VMware Workstation
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1242/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of VMware Workstation. An attacker must first obtain the ability to execute low-privileged code on the guest system in order to exploit this vulnerability. The specific flaw exists within the handling of virtualized SVGA. The issue results from the lack of proper validation of user-supplied data, which can result in an overflow of a heap-based buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the host OS.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2018-0026.html

## Disclosure Timeline

- 2018-06-12 - Vulnerability reported to vendor
- 2018-10-16 - Coordinated public release of advisory
- 2018-10-16 - Advisory Updated
