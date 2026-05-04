# ZDI-19-917: Oracle VirtualBox VMSVGA Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-917
- **ZDI-CAN:** ZDI-CAN-8652
- **Date:** 2019-10-23
- **CVE:** CVE-2019-3026
- **CVSS:** 6.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** anhdaden of STAR Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-917/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the vmsvgaFIFOLoop function. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuoct2019.html

## Disclosure Timeline

- 2019-08-13 - Vulnerability reported to vendor
- 2019-10-23 - Coordinated public release of advisory
