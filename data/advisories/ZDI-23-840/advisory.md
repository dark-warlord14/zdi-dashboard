# ZDI-23-840: VMware Aria Operations for Networks createSupportBundle Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-840
- **ZDI-CAN:** ZDI-CAN-19980
- **Date:** 2023-06-08
- **CVE:** CVE-2023-20887
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** VMware
- **Affected Products:** Aria Operations for Networks
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-840/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of VMware Aria Operations for Networks. Authentication is not required to exploit this vulnerability. The specific flaw exists within the createSupportBundle method. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2023-0012.html

## Disclosure Timeline

- 2023-02-08 - Vulnerability reported to vendor
- 2023-06-08 - Coordinated public release of advisory
