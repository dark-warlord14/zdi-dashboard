# ZDI-20-582: (Pwn2Own) Oracle VirtualBox OHCI Uninitialized Variable Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-582
- **ZDI-CAN:** ZDI-CAN-10783
- **Date:** 2020-04-30
- **CVE:** CVE-2020-2575
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** anhdaden of STAR Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-582/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the processing of data sent to OHCI endpoints. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2020.html

## Disclosure Timeline

- 2020-04-30 - Vulnerability reported to vendor
- 2020-04-30 - Coordinated public release of advisory
