# ZDI-22-805: KeySight N6841A RF Sensor UserFirmwareRequestHandler Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-805
- **ZDI-CAN:** ZDI-CAN-15525
- **Date:** 2022-05-27
- **CVE:** CVE-2022-1661
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** KeySight
- **Affected Products:** N6841A RF Sensor
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-805/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of KeySight N6841A RF Sensor. Authentication is not required to exploit this vulnerability. The specific flaw exists within the UserFirmwareRequestHandler class. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose files in the context of SYSTEM.

## Additional Details

KeySight has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-146-01

## Disclosure Timeline

- 2021-12-30 - Vulnerability reported to vendor
- 2022-05-27 - Coordinated public release of advisory
