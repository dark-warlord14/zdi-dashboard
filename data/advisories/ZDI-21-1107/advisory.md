# ZDI-21-1107: VMware vCenter Server Appliance Missing Authentication Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1107
- **ZDI-CAN:** ZDI-CAN-13633
- **Date:** 2021-09-22
- **CVE:** CVE-2021-22008
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** VMware
- **Affected Products:** vCenter Server Appliance
- **Credit:** Sergey Gerasimov and George webpentest Noseevich of SolidLab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1107/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of VMware vCenter Server Appliance. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of jsonrpc messages. The issue results from the lack of proper authentication before processing messages. An attacker can leverage this vulnerability to disclose sensitive information from the server.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2021-0020.html

## Disclosure Timeline

- 2021-05-26 - Vulnerability reported to vendor
- 2021-09-22 - Coordinated public release of advisory
