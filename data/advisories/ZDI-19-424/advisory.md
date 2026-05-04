# ZDI-19-424: (Pwn2Own) Oracle VirtualBox e1000 Race Condition Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-424
- **ZDI-CAN:** ZDI-CAN-8362
- **Date:** 2019-04-29
- **CVE:** CVE-2019-2723
- **CVSS:** 6.7
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** fluoroacetate (@fluoroacetate)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-424/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Oracle VirtualBox. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of virtualized e1000 devices. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/technetwork/security-advisory/cpuapr2019-5072813.html

## Disclosure Timeline

- 2019-03-20 - Vulnerability reported to vendor
- 2019-04-29 - Coordinated public release of advisory
- 2019-06-14 - Advisory Updated
