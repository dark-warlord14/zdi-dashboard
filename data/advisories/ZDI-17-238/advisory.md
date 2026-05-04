# ZDI-17-238: (Pwn2Own) VMware Workstation Uninitialized Memory Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-238
- **ZDI-CAN:** ZDI-CAN-4631
- **Date:** 2017-03-30
- **CVE:** CVE-2017-4905
- **CVSS:** 4.9
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** VMware
- **Affected Products:** VMware Workstation
- **Credit:** Tencent Security - Team Sniper (Keen Lab and PC Mgr)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-238/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of VMware Workstation. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of the Backdoor communications channel. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the hypervisor.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: http://www.vmware.com/security/advisories/VMSA-2017-0006.html

## Disclosure Timeline

- 2017-03-18 - Vulnerability reported to vendor
- 2017-03-30 - Coordinated public release of advisory
