# ZDI-21-207: SolarWinds Patch Manager DataGridService Deserialization of Untrusted Data Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-207
- **ZDI-CAN:** ZDI-CAN-12009
- **Date:** 2021-02-24
- **CVE:** CVE-2021-27240
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Patch Manager
- **Credit:** Harrison Neal
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-207/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of SolarWinds Patch Manager. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the DataGridService WCF service. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of Administrator.

## Additional Details

Fixed in Patch Manager v2020.2.4

## Disclosure Timeline

- 2020-11-13 - Vulnerability reported to vendor
- 2021-02-24 - Coordinated public release of advisory
