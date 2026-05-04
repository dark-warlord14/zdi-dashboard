# ZDI-21-1105: VMware vCenter Server Appliance Update Manager Directory Traversal Arbitrary File Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1105
- **ZDI-CAN:** ZDI-CAN-13425
- **Date:** 2021-09-22
- **CVE:** CVE-2021-22018
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:L
- **Affected Vendors:** VMware
- **Affected Products:** vCenter Server Appliance
- **Credit:** Sergey Gerasimov of Solidlab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1105/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files on affected installations of VMware vCenter Server Appliance. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Update Manager. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to delete files in the context of the service account.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2021-0020.html

## Disclosure Timeline

- 2021-05-18 - Vulnerability reported to vendor
- 2021-09-22 - Coordinated public release of advisory
