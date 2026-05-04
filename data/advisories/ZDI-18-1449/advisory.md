# ZDI-18-1449: Oracle VirtualBox crUnpackMap2d Integer Overflow Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1449
- **ZDI-CAN:** ZDI-CAN-7228
- **Date:** 2019-01-24
- **CVE:** CVE-2018-3293
- **CVSS:** 3.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:L/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Root Object
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1449/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of Oracle VirtualBox. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the crUnpackMap2d method. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/technetwork/security-advisory/cpuoct2018-4428296.html

## Disclosure Timeline

- 2018-09-10 - Vulnerability reported to vendor
- 2019-01-24 - Coordinated public release of advisory
