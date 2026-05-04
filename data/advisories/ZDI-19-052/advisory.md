# ZDI-19-052: Oracle VirtualBox crServerDispatchGetMapfv Uninitialized Memory Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-052
- **ZDI-CAN:** ZDI-CAN-7447
- **Date:** 2019-01-17
- **CVE:** CVE-2019-2554
- **CVSS:** 6.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** An Example
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-052/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of Oracle VirtualBox. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the crServerDispatchGetMapfv method. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/technetwork/security-advisory/cpujan2019-5072801.html

## Disclosure Timeline

- 2018-11-05 - Vulnerability reported to vendor
- 2019-01-17 - Coordinated public release of advisory
