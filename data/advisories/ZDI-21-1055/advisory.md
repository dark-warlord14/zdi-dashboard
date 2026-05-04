# ZDI-21-1055: Parallels Desktop Toolgate Uncontrolled Memory Allocation Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1055
- **ZDI-CAN:** ZDI-CAN-13672
- **Date:** 2021-09-08
- **CVE:** CVE-2021-34867
- **CVSS:** 7.5
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** Reno Robert of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1055/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the Toolgate component. The issue results from the lack of proper validation of user-supplied data, which can result in an uncontrolled memory allocation. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

Parallels has issued an update to correct this vulnerability. More details can be found at: https://kb.parallels.com/125013

## Disclosure Timeline

- 2021-04-16 - Vulnerability reported to vendor
- 2021-09-08 - Coordinated public release of advisory
