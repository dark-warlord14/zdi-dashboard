# ZDI-19-392: Oracle VirtualBox crServerDispatchGetFinalCombinerInputParameterivNV Uninitialized Memory Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-392
- **ZDI-CAN:** ZDI-CAN-7893
- **Date:** 2019-04-17
- **CVE:** CVE-2019-2574
- **CVSS:** 6.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** huyna of Viettel Cyber Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-392/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of Oracle VirtualBox. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the crServerDispatchGetFinalCombinerInputParameterivNV method. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/technetwork/security-advisory/cpuapr2019-5072813.html

## Disclosure Timeline

- 2019-01-21 - Vulnerability reported to vendor
- 2019-04-17 - Coordinated public release of advisory
