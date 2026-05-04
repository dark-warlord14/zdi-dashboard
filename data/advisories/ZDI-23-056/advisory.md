# ZDI-23-056: VMware vRealize Network Insight downloadFile Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-056
- **ZDI-CAN:** ZDI-CAN-17960
- **Date:** 2023-01-18
- **CVE:** CVE-2022-31703
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** VMware
- **Affected Products:** vRealize
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-056/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of VMware vRealize Network Insight. Authentication is not required to exploit this vulnerability. The specific flaw exists within the downloadFile function. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of the service account.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2022-0031.html

## Disclosure Timeline

- 2022-08-31 - Vulnerability reported to vendor
- 2023-01-18 - Coordinated public release of advisory
