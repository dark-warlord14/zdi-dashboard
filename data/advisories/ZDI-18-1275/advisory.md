# ZDI-18-1275: Oracle VirtualBox crServerDispatchGenTextures Integer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1275
- **ZDI-CAN:** ZDI-CAN-6665
- **Date:** 2018-10-17
- **CVE:** CVE-2018-3298
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** hysterical raisins
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1275/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Oracle VirtualBox. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the crServerDispatchGenTextures method. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/technetwork/security-advisory/cpuoct2018-4428296.html

## Disclosure Timeline

- 2018-07-09 - Vulnerability reported to vendor
- 2018-10-17 - Coordinated public release of advisory
