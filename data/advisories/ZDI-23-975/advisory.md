# ZDI-23-975: KeySight N6841A RF Sensor smsRestoreDatabaseZip Exposed Dangerous Function Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-975
- **ZDI-CAN:** ZDI-CAN-19095
- **Date:** 2023-07-19
- **CVE:** CVE-2023-36853
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** KeySight
- **Affected Products:** N6841A RF Sensor
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-975/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of KeySight N6841A RF Sensor. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the smsRestoreDatabaseZip function. The issue results from an exposed dangerous function. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

KeySight has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-23-199-02

## Disclosure Timeline

- 2022-11-03 - Vulnerability reported to vendor
- 2023-07-19 - Coordinated public release of advisory
