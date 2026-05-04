# ZDI-17-738: VMware Workstation Shader Out-Of-Bounds Write Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-738
- **ZDI-CAN:** ZDI-CAN-4857
- **Date:** 2017-09-15
- **CVE:** CVE-2017-4924
- **CVSS:** 6.2
- **CVSS Vector:** AV:L/AC:H/Au:N/C:C/I:C/A:C
- **Affected Vendors:** VMware
- **Affected Products:** VMware Workstation
- **Credit:** Nico Golde and Ralf-Philipp Weinmann Comsecuris UG (haftungsbeschraenkt)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-738/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of VMware Workstation. An attacker must first obtain the ability to execute low-privileged code on the guest system in order to exploit this vulnerability. The specific flaw exists within the Shader implementation. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the host OS.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2017-0015.html

## Disclosure Timeline

- 2017-06-22 - Vulnerability reported to vendor
- 2017-09-15 - Coordinated public release of advisory
