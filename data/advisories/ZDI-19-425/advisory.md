# ZDI-19-425: (Pwn2Own) Oracle VirtualBox e1000 Integer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-425
- **ZDI-CAN:** ZDI-CAN-8363
- **Date:** 2019-04-29
- **CVE:** CVE-2019-2722
- **CVSS:** 6.7
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** anhdaden of StarLabs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-425/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Oracle VirtualBox. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of virtualized e1000 devices. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/technetwork/security-advisory/cpuapr2019-5072813.html

## Disclosure Timeline

- 2019-03-20 - Vulnerability reported to vendor
- 2019-04-29 - Coordinated public release of advisory
- 2021-06-29 - Advisory Updated
