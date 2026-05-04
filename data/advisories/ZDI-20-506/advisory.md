# ZDI-20-506: Oracle VirtualBox vmsvgaR3FifoUpdateCursor Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-506
- **ZDI-CAN:** ZDI-CAN-10422
- **Date:** 2020-04-16
- **CVE:** CVE-2020-2748
- **CVSS:** 3.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:L/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** anhdaden & Calvin Fong (Lord_Idiot) of STAR Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-506/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the vmsvgaR3FifoUpdateCursor function. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2020.html

## Disclosure Timeline

- 2020-03-03 - Vulnerability reported to vendor
- 2020-04-16 - Coordinated public release of advisory
