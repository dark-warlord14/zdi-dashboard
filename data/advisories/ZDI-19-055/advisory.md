# ZDI-19-055: Oracle VirtualBox crServerDispatchGetActiveUniform Integer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-055
- **ZDI-CAN:** ZDI-CAN-7210
- **Date:** 2019-01-17
- **CVE:** CVE-2019-2526
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-055/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Oracle VirtualBox. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the crServerDispatchGetActiveUniform method. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/technetwork/security-advisory/cpujan2019-5072801.html

## Disclosure Timeline

- 2018-09-05 - Vulnerability reported to vendor
- 2019-01-17 - Coordinated public release of advisory
