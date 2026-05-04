# ZDI-19-053: Oracle VirtualBox crServerDispatchGetMapiv Uninitialized Memory Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-053
- **ZDI-CAN:** ZDI-CAN-7448
- **Date:** 2019-01-17
- **CVE:** CVE-2019-2451
- **CVSS:** 6.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Ex Allocate Pool With Tag
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-053/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of Oracle VirtualBox. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the crServerDispatchGetMapiv method. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/technetwork/security-advisory/cpujan2019-5072801.html

## Disclosure Timeline

- 2018-11-05 - Vulnerability reported to vendor
- 2019-01-17 - Coordinated public release of advisory
