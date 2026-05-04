# ZDI-20-135: Oracle VirtualBox e1000 Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-135
- **ZDI-CAN:** ZDI-CAN-9457
- **Date:** 2020-01-15
- **CVE:** CVE-2020-2693
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Instructor
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-135/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the e1000 virtual device. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujan2020.html

## Disclosure Timeline

- 2019-11-12 - Vulnerability reported to vendor
- 2020-01-15 - Coordinated public release of advisory
