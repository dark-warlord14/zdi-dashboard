# ZDI-24-882: VMware vCenter Server Appliance License Server Uncontrolled Memory Allocation Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-882
- **ZDI-CAN:** ZDI-CAN-20007
- **Date:** 2024-06-25
- **CVE:** CVE-2024-37087
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L
- **Affected Vendors:** VMware
- **Affected Products:** vCenter Server Appliance
- **Credit:** Guy Lederfein of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-882/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of VMware vCenter Server Appliance. Authentication is not required to exploit this vulnerability. The specific flaw exists within the License Server. The issue results from the lack of proper validation of user-supplied data, which can result in an uncontrolled memory allocation. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/24505

## Disclosure Timeline

- 2023-01-05 - Vulnerability reported to vendor
- 2024-06-25 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
