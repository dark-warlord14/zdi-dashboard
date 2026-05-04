# ZDI-21-192: SolarWinds Orion Platform NCM SCM IPAM SaveUserSetting Improper Access Control Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-192
- **ZDI-CAN:** ZDI-CAN-11903
- **Date:** 2021-12-08
- **CVE:** CVE-2021-27258
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Orion Platform
- **Credit:** Piotr Bazydlo (@chudypb)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-192/
## Vulnerability Details

This vulnerability allows remote attackers to execute escalate privileges on affected installations of SolarWinds Orion Platform. Authentication is not required to exploit this vulnerability. The specific flaw exists within the SaveUserSetting endpoint. The issue results from improper restriction of this endpoint to unprivileged users. An attacker can leverage this vulnerability to escalate privileges their privileges from Guest to Administrator.

## Additional Details

Fixed in our Orion Platform 2020.2.4

## Disclosure Timeline

- 2020-10-09 - Vulnerability reported to vendor
- 2021-12-08 - Coordinated public release of advisory
- 2022-05-26 - Advisory Updated
