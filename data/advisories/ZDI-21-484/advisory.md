# ZDI-21-484: (Pwn2Own) Oracle VirtualBox SLiRP Networking Heap-based Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-484
- **ZDI-CAN:** ZDI-CAN-13568
- **Date:** 2021-04-28
- **CVE:** CVE-2021-2250
- **CVSS:** 7.5
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** STARLabs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-484/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the parsing of ICMP messages. The issue results from the lack of proper validation of guest-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2021.html

## Disclosure Timeline

- 2021-04-22 - Vulnerability reported to vendor
- 2021-04-28 - Coordinated public release of advisory
