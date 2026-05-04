# ZDI-21-1244: SolarWinds Orion Platform NCM SCM IPAM SaveUserSetting Improper Access Control Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1244
- **ZDI-CAN:** ZDI-CAN-13453
- **Date:** 2021-10-28
- **CVE:** CVE-2021-35213
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Orion Platform
- **Credit:** Piotr Bazydlo (@chudypb)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1244/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of SolarWinds Orion Platform. Authentication is required to exploit this vulnerability. The specific flaw exists within the SaveUserSetting endpoint. The issue results from improper control of access to this endpoint. An attacker can leverage this vulnerability to escalate privileges from Guest to Administrator.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://www.solarwinds.com/trust-center/security-advisories/cve-2021-35213

## Disclosure Timeline

- 2021-05-05 - Vulnerability reported to vendor
- 2021-10-28 - Coordinated public release of advisory
- 2022-05-26 - Advisory Updated
