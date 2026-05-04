# ZDI-24-526: (Pwn2Own) VMware Workstation VBluetoothHCI_PacketOut Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-526
- **ZDI-CAN:** ZDI-CAN-23844
- **Date:** 2024-05-30
- **CVE:** CVE-2024-22267
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** VMware
- **Affected Products:** Workstation
- **Credit:** Gwangun Jung(@pr0ln) and Junoh Lee(@bbbig12) at Theori(@theori_io)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-526/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of VMware Workstation. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the VBluetoothHCI_PacketOut function. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/24280

## Disclosure Timeline

- 2024-04-29 - Vulnerability reported to vendor
- 2024-05-30 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
