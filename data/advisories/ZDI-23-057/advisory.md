# ZDI-23-057: VMware vRealize Operations CaSA Improper Access Control Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-057
- **ZDI-CAN:** ZDI-CAN-18336
- **Date:** 2023-01-18
- **CVE:** CVE-2022-31708
- **CVSS:** 4.9
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** VMware
- **Affected Products:** vRealize
- **Credit:** Reno Robert of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-057/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of VMware vRealize Operations. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the configuration of CaSA. The issue results from the lack of proper access control. An attacker can leverage this vulnerability to disclose information in the context of root.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2022-0034.html

## Disclosure Timeline

- 2022-08-31 - Vulnerability reported to vendor
- 2023-01-18 - Coordinated public release of advisory
