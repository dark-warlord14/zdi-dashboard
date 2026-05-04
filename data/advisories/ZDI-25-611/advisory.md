# ZDI-25-611: VMware ESXi VMCI Uninitialized Memory Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-611
- **ZDI-CAN:** ZDI-CAN-27123
- **Date:** 2025-07-17
- **CVE:** CVE-2025-41239
- **CVSS:** 6.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** VMware
- **Affected Products:** ESXi
- **Credit:** Gwangun Jung at THEORI
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-611/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of VMware ESXi. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the implementation of VMCI. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the host.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/35877

## Disclosure Timeline

- 2025-05-08 - Vulnerability reported to vendor
- 2025-07-17 - Coordinated public release of advisory
- 2025-07-17 - Advisory Updated
