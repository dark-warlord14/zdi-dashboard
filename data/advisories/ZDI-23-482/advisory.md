# ZDI-23-482: VMware Aria Operations for Logs Cluster Controller Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-482
- **ZDI-CAN:** ZDI-CAN-20380
- **Date:** 2023-04-24
- **CVE:** CVE-2023-20864
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** VMware
- **Affected Products:** Aria Operations for Logs
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-482/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of VMware Aria Operations for Logs. Authentication is not required to exploit this vulnerability. The specific flaw exists within the InternalClusterController class. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2023-0007.html

## Disclosure Timeline

- 2023-02-24 - Vulnerability reported to vendor
- 2023-04-24 - Coordinated public release of advisory
