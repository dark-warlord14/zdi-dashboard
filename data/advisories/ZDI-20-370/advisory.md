# ZDI-20-370: Schneider Electric IGSS IGSSupdateservice Improper Access Control Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-370
- **ZDI-CAN:** ZDI-CAN-9758
- **Date:** 2020-04-03
- **CVE:** CVE-2020-7479
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** IGSS
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-370/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Schneider Electric IGSS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the IGSSupdateservice service, which listens on TCP port 12414 by default. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-20-084-02

## Disclosure Timeline

- 2019-12-10 - Vulnerability reported to vendor
- 2020-04-03 - Coordinated public release of advisory
