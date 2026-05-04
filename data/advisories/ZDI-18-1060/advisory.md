# ZDI-18-1060: VMware Workstation e1000 Buffer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1060
- **ZDI-CAN:** ZDI-CAN-6364
- **Date:** 2018-09-17
- **CVE:** CVE-2018-6973
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** VMware
- **Affected Products:** VMware Workstation
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1060/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of VMware Workstation. An attacker must first obtain the ability to execute low-privileged code on the guest system in order to exploit this vulnerability. The specific flaw exists within the handling of the virtualized e1000 device. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the host OS.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2018-0022.html

## Disclosure Timeline

- 2018-06-12 - Vulnerability reported to vendor
- 2018-09-17 - Coordinated public release of advisory
- 2018-09-17 - Advisory Updated
