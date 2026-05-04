# ZDI-21-1223: Linux Kernel Bluetooth CMTP Module Double Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1223
- **ZDI-CAN:** ZDI-CAN-11977
- **Date:** 2021-10-21
- **CVE:** CVE-2021-34981
- **CVSS:** 7.5
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Ryota Shiga(@Ga_ryo_) of Flatt Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1223/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the CMTP module. The issue results from the lack of validating the existence of an object prior to performing further free operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the kernel.

## Additional Details

Fixed in version 5.10.42

## Disclosure Timeline

- 2021-04-23 - Vulnerability reported to vendor
- 2021-10-21 - Coordinated public release of advisory
