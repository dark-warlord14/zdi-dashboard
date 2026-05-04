# ZDI-23-974: KeySight N6841A RF Sensor removeLicenseFile Directory Traversal Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-974
- **ZDI-CAN:** ZDI-CAN-18753
- **Date:** 2023-07-19
- **CVE:** CVE-2023-34394
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** KeySight
- **Affected Products:** N6841A RF Sensor
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-974/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of KeySight N6841A RF Sensor. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the removeLicenseFile class. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

KeySight has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-23-199-02

## Disclosure Timeline

- 2022-10-06 - Vulnerability reported to vendor
- 2023-07-19 - Coordinated public release of advisory
