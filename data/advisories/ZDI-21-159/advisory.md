# ZDI-21-159: QEMU Plan 9 File System Time-Of-Check Time-Of-Use Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-159
- **ZDI-CAN:** ZDI-CAN-10904
- **Date:** 2021-02-10
- **CVE:** CVE-2021-20181
- **CVSS:** 7.5
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** QEMU
- **Affected Products:** QEMU
- **Credit:** Ryota Shiga(@Ga_ryo_) of Flatt Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-159/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on affected installations of QEMU. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the handling of file descriptor maps. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

QEMU has issued an update to correct this vulnerability. More details can be found at: https://bugs.launchpad.net/qemu/+bug/1911666

## Disclosure Timeline

- 2020-12-18 - Vulnerability reported to vendor
- 2021-02-10 - Coordinated public release of advisory
