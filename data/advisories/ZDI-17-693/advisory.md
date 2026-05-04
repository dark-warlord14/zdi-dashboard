# ZDI-17-693: Bitdefender Total Security bdfwfpf Kernel Driver Double Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-693
- **ZDI-CAN:** ZDI-CAN-4776
- **Date:** 2017-08-17
- **CVE:** CVE-2017-10950
- **CVSS:** 6.2
- **CVSS Vector:** AV:L/AC:H/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Bitdefender
- **Affected Products:** Total Security
- **Credit:** bee13oy of CloverSec Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-693/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Bitdefender Total Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within processing of the 0x8000E038 IOCTL in the bdfwfpf driver. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker could leverage this vulnerability to execute arbitrary code in the context of SYSTEM.

## Additional Details

On AV 2017, build version: 21.2.25.30; On AV 2018, build version starting from 22.0.8.114.

## Disclosure Timeline

- 2017-05-04 - Vulnerability reported to vendor
- 2017-08-17 - Coordinated public release of advisory
