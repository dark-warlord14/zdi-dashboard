# ZDI-18-691: Oracle VirtualBox SHCRGL_GUEST_FN_WRITE_READ_BUFFERED Uninitialized Memory Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-691
- **ZDI-CAN:** ZDI-CAN-6114
- **Date:** 2018-07-18
- **CVE:** CVE-2018-3091
- **CVSS:** 4.7
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Niklas Baumstark
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-691/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of Oracle VirtualBox. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the SHCRGL_GUEST_FN_WRITE_READ_BUFFERED method. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute code under the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/security-advisory/cpujul2018-4258247.html

## Disclosure Timeline

- 2018-06-08 - Vulnerability reported to vendor
- 2018-07-18 - Coordinated public release of advisory
- 2018-07-18 - Advisory Updated
