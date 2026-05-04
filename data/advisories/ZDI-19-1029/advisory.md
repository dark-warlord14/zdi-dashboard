# ZDI-19-1029: Docker docker-credential-helpers Double Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-1029
- **ZDI-CAN:** ZDI-CAN-8920
- **Date:** 2019-12-20
- **CVE:** CVE-2019-17149
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Docker
- **Affected Products:** Docker
- **Credit:** Jasiel Spelman of Trend Micro Zero Day Initiative and Trend Micro Team Nebula
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-1029/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Docker. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within docker-credential-helpers. The issue results from the lack of validating the existence of an object prior to performing further free operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the application.

## Additional Details

Fixed in version 0.6.3

## Disclosure Timeline

- 2019-06-27 - Vulnerability reported to vendor
- 2019-12-20 - Coordinated public release of advisory
