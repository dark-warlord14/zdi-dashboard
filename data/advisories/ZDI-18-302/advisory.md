# ZDI-18-302: Oracle VirtualBox crUnpackExtendProgramParameters4fvNV Integer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-302
- **ZDI-CAN:** ZDI-CAN-5155
- **Date:** 2018-04-18
- **CVE:** CVE-2018-2830
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Vasily Vasiliev
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-302/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Oracle VirtualBox. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the crUnpackExtendProgramParameters4fvNV method. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to escalate privileges and execute code under the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/security-advisory/cpuapr2018-3678067.html

## Disclosure Timeline

- 2018-01-26 - Vulnerability reported to vendor
- 2018-04-18 - Coordinated public release of advisory
- 2018-04-18 - Advisory Updated
