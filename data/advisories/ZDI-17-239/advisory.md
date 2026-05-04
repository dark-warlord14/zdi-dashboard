# ZDI-17-239: (Pwn2Own) VMware Workstation Uninitialized Memory Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-239
- **ZDI-CAN:** ZDI-CAN-4632
- **Date:** 2017-03-30
- **CVE:** CVE-2017-4904
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** VMware
- **Affected Products:** VMware Workstation
- **Credit:** Tencent Security - Team Sniper (Keen Lab and PC Mgr)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-239/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of VMware Workstation. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of XHCI communication. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this vulnerability to elevate privileges and execute arbitrary code under the context of the hypervisor.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: http://www.vmware.com/security/advisories/VMSA-2017-0006.html

## Disclosure Timeline

- 2017-03-18 - Vulnerability reported to vendor
- 2017-03-30 - Coordinated public release of advisory
