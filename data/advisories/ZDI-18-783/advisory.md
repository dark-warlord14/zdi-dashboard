# ZDI-18-783: (Pwn2Own) Oracle Virtualbox HGCM Out-Of-Bounds Write Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-783
- **ZDI-CAN:** ZDI-CAN-5818
- **Date:** 2018-07-26
- **CVE:** CVE-2018-2860
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Niklas Baumstark from team phoenhex
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-783/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on vulnerable installations of Oracle VirtualBox. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the handling of HGCM. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated object. An attacker can leverage this vulnerability to execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/security-advisory/cpuapr2018-3678067.html

## Disclosure Timeline

- 2018-02-20 - Vulnerability reported to vendor
- 2018-07-26 - Coordinated public release of advisory
- 2018-07-26 - Advisory Updated
