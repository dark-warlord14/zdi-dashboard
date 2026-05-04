# ZDI-19-306: VMware Workstation e1000 Out-Of-Bounds Write Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-306
- **ZDI-CAN:** ZDI-CAN-7450
- **Date:** 2019-04-02
- **CVE:** CVE-2019-5515
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:L/I:L/A:L
- **Affected Vendors:** VMware
- **Affected Products:** Workstation
- **Credit:** instructor
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-306/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of VMware Workstation. An attacker must first obtain the ability to execute low-privileged code on the guest system in order to exploit this vulnerability. The specific flaw exists within the handling of virtualized e1000 devices. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the host OS.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2019-0005.html

## Disclosure Timeline

- 2018-11-06 - Vulnerability reported to vendor
- 2019-04-02 - Coordinated public release of advisory
