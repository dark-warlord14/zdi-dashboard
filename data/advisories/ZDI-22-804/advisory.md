# ZDI-22-804: KeySight N6841A RF Sensor Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-804
- **ZDI-CAN:** ZDI-CAN-15470
- **Date:** 2022-05-27
- **CVE:** CVE-2022-1660
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** KeySight
- **Affected Products:** N6841A RF Sensor
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-804/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of KeySight N6841A RF Sensor. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of Spring Framework. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

KeySight has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-146-01

## Disclosure Timeline

- 2021-12-30 - Vulnerability reported to vendor
- 2022-05-27 - Coordinated public release of advisory
