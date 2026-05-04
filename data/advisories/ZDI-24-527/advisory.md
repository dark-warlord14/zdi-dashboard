# ZDI-24-527: (Pwn2Own) VMWare Workstation VBluetoothHCI_PacketOut Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-527
- **ZDI-CAN:** ZDI-CAN-23847
- **Date:** 2024-05-31
- **CVE:** CVE-2024-22267
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** VMware
- **Affected Products:** Workstation
- **Credit:** Nguy\xe1\xbb\x85n Ho\xc3\xa0ng Th\xe1\xba\xa1ch of STAR Labs SG Pte. Ltd.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-527/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of VMWare Workstation. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the VBluetoothHCI_PacketOut method. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/24280

## Disclosure Timeline

- 2024-04-29 - Vulnerability reported to vendor
- 2024-05-31 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
