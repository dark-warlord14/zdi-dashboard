# ZDI-23-1590: VMware vCenter Server Appliance DCE/RPC Protocol Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1590
- **ZDI-CAN:** ZDI-CAN-21893
- **Date:** 2023-11-06
- **CVE:** CVE-2023-34048
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** VMware
- **Affected Products:** vCenter Server Appliance
- **Credit:** Grigory Dorodnov of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1590/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of VMware vCenter Server Appliance. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of DCE/RPC protocol. The issue results from the lack of proper validation of user-supplied data, which can result in a write before the start of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2023-0023.html

## Disclosure Timeline

- 2023-08-16 - Vulnerability reported to vendor
- 2023-11-06 - Coordinated public release of advisory
