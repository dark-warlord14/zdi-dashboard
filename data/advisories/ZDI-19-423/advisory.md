# ZDI-19-423: (Pwn2Own) Oracle VirtualBox OHCI Integer Overflow Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-423
- **ZDI-CAN:** ZDI-CAN-8361
- **Date:** 2019-04-29
- **CVE:** CVE-2019-2723
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:R/S:U/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** fluoroacetate (@fluoroacetate)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-423/
## Vulnerability Details

Workstation This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of Oracle VirtualBox. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the processing of OHCI data. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/technetwork/security-advisory/cpuapr2019-5072813.html

## Disclosure Timeline

- 2019-03-20 - Vulnerability reported to vendor
- 2019-04-29 - Coordinated public release of advisory
- 2019-06-14 - Advisory Updated
