# ZDI-20-198: Bitdefender Total Security Link Resolution Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-198
- **ZDI-CAN:** ZDI-CAN-8956
- **Date:** 2020-02-05
- **CVE:** CVE-2020-8095
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Bitdefender
- **Affected Products:** Total Security
- **Credit:** Nabeel Ahmed of Dimension Data Belgium
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-198/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of BitDefender Total Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of junctions. By creating a junction, an attacker can abuse the service to delete arbitrary files. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Bitdefender has issued an update to correct this vulnerability. More details can be found at: https://www.bitdefender.com/support/security-advisories/bitdefender-total-security-link-resolution-denial-service-vulnerability-va-4021/

## Disclosure Timeline

- 2019-08-29 - Vulnerability reported to vendor
- 2020-02-05 - Coordinated public release of advisory
