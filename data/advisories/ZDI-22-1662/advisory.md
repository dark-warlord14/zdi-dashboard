# ZDI-22-1662: SolarWinds Network Performance Monitor WebUserSettingsCrudHandler Improper Input Validation Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1662
- **ZDI-CAN:** ZDI-CAN-17644
- **Date:** 2022-11-23
- **CVE:** CVE-2022-36960
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Network Performance Monitor
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1662/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of SolarWinds Network Performance Monitor. Authentication is required to exploit this vulnerability. The specific flaw exists within the CheckWhetherNonAdminAttemptsToModifyBlacklistedRecords function. The issue results from the lack of proper validation of the user-supplied SettingName parameter. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://www.solarwinds.com/trust-center/security-advisories/cve-2022-36960

## Disclosure Timeline

- 2022-06-07 - Vulnerability reported to vendor
- 2022-11-23 - Coordinated public release of advisory
