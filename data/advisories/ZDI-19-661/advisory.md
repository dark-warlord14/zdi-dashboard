# ZDI-19-661: Oracle VirtualBox cr_unpackData Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-661
- **ZDI-CAN:** ZDI-CAN-7159
- **Date:** 2019-07-22
- **CVE:** CVE-2019-2863
- **CVSS:** 6.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Jason Matthyser of MWR Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-661/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the cr_unpackData method. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/technetwork/security-advisory/cpujul2019-5072835.html

## Disclosure Timeline

- 2019-01-02 - Vulnerability reported to vendor
- 2019-07-22 - Coordinated public release of advisory
