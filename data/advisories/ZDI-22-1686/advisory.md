# ZDI-22-1686: VMware ESXi TCP/IP Memory Corruption Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1686
- **ZDI-CAN:** ZDI-CAN-17737
- **Date:** 2022-12-21
- **CVE:** CVE-2022-31696
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** VMware
- **Affected Products:** ESXi
- **Credit:** Reno Robert of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1686/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of VMware ESXi. An attacker must first obtain the ability to execute low-privileged code on the target host system in order to exploit this vulnerability. The specific flaw exists within the TCPIP kernel module. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of kernel.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2022-0030.html

## Disclosure Timeline

- 2022-06-28 - Vulnerability reported to vendor
- 2022-12-21 - Coordinated public release of advisory
