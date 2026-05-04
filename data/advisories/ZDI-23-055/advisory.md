# ZDI-23-055: VMware vRealize Network Insight createSupportBundle Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-055
- **ZDI-CAN:** ZDI-CAN-17959
- **Date:** 2023-01-18
- **CVE:** CVE-2022-31702
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** VMware
- **Affected Products:** vRealize
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-055/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of VMware vRealize Network Insight. Authentication is not required to exploit this vulnerability. The specific flaw exists within the createSupportBundle function. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2022-0031.html

## Disclosure Timeline

- 2022-08-31 - Vulnerability reported to vendor
- 2023-01-18 - Coordinated public release of advisory
