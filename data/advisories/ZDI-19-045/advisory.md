# ZDI-19-045: Oracle VirtualBox crUnpackExtendGetAttribLocation Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-045
- **ZDI-CAN:** ZDI-CAN-7330
- **Date:** 2019-01-17
- **CVE:** CVE-2019-2525
- **CVSS:** 5.6
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Jason Matthyser (@pleasew8t) of MWR Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-045/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Oracle VirtualBox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the crUnpackExtendGetAttribLocation method. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/technetwork/security-advisory/cpujan2019-5072801.html

## Disclosure Timeline

- 2018-10-04 - Vulnerability reported to vendor
- 2019-01-17 - Coordinated public release of advisory
