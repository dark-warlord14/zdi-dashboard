# ZDI-20-199: Google Android V4l2 cam_actuator_driver_cmd Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-199
- **ZDI-CAN:** ZDI-CAN-9549
- **Date:** 2020-02-07
- **CVE:** CVE-2019-14088
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Google
- **Affected Products:** Android
- **Credit:** Lacne Jiang and Moony Li of TrendMicro Mobile Security Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-199/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Google Android. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the cam_actuator_driver_cmd function in the V4l2 driver. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the kernel.

## Additional Details

Google has issued an update to correct this vulnerability. More details can be found at: https://source.android.com/security/bulletin/pixel/2020-02-01.html

## Disclosure Timeline

- 2019-10-18 - Vulnerability reported to vendor
- 2020-02-07 - Coordinated public release of advisory
