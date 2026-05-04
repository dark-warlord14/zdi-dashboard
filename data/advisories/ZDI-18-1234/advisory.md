# ZDI-18-1234: Oracle VirtualBox crUnpackExtendAreProgramsResidentNV Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1234
- **ZDI-CAN:** ZDI-CAN-6592
- **Date:** 2018-10-15
- **CVE:** CVE-2018-3055
- **CVSS:** 4.7
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Add of MeePwn
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1234/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of Oracle VirtualBox. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the crUnpackExtendAreProgramsResidentNV method. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/technetwork/security-advisory/cpujul2018-4258247.html

## Disclosure Timeline

- 2018-07-10 - Vulnerability reported to vendor
- 2018-10-15 - Coordinated public release of advisory
- 2018-10-15 - Advisory Updated
