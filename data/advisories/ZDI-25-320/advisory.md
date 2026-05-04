# ZDI-25-320: SolarWinds DameWare Mini Remote Control Service Incorrect Permissions Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-320
- **ZDI-CAN:** ZDI-CAN-26279
- **Date:** 2025-06-02
- **CVE:** CVE-2025-26396
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** DameWare Mini Remote Control
- **Credit:** Alexander Pudwill
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-320/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of SolarWinds DameWare Mini Remote Control Service. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the product installer. The issue results from incorrect permissions on a folder used by the product. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://documentation.solarwinds.com/en/success_center/dameware/content/release_notes/dameware_12-3-2_release_notes.htm

## Disclosure Timeline

- 2025-03-04 - Vulnerability reported to vendor
- 2025-06-02 - Coordinated public release of advisory
- 2025-06-02 - Advisory Updated
