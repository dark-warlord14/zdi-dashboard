# ZDI-19-048: Oracle VirtualBox crUnpackExtendGetUniformLocation Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-048
- **ZDI-CAN:** ZDI-CAN-6964
- **Date:** 2019-01-17
- **CVE:** CVE-2019-2448
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Niklas Baumstark
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-048/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of Oracle VirtualBox. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the crUnpackExtendGetUniformLocation method. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/technetwork/security-advisory/cpujan2019-5072801.html

## Disclosure Timeline

- 2018-12-18 - Vulnerability reported to vendor
- 2019-01-17 - Coordinated public release of advisory
- 2021-06-29 - Advisory Updated
