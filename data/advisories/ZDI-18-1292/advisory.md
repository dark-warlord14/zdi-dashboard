# ZDI-18-1292: Oracle VirtualBox crServerDispatchReadPixels Integer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1292
- **ZDI-CAN:** ZDI-CAN-7329
- **Date:** 2018-10-18
- **CVE:** CVE-2018-3293
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:C/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Root Object
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1292/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Oracle VirtualBox. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the crServerDispatchReadPixels method. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/technetwork/security-advisory/cpuoct2018-4428296.html

## Disclosure Timeline

- 2018-10-03 - Vulnerability reported to vendor
- 2018-10-18 - Coordinated public release of advisory
