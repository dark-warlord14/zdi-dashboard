# ZDI-24-528: (Pwn2Own) VMware Workstation hgfsVMCI_fileread Use of Uninitialized Variable Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-528
- **ZDI-CAN:** ZDI-CAN-23783
- **Date:** 2024-05-31
- **CVE:** CVE-2024-22270
- **CVSS:** 6.0
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** VMware
- **Affected Products:** Workstation
- **Credit:** Gwangun Jung(@pr0ln) and Junoh Lee(@bbbig12) at Theori(@theori_io)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-528/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of VMware Workstation. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the hgfsVMCI_fileread function. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/24280

## Disclosure Timeline

- 2024-04-29 - Vulnerability reported to vendor
- 2024-05-31 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
