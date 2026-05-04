# ZDI-22-1325: SolarWinds Network Performance Monitor UpdateActionsDescriptions SQL Injection Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1325
- **ZDI-CAN:** ZDI-CAN-17666
- **Date:** 2022-09-30
- **CVE:** CVE-2022-36961
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Network Performance Monitor
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1325/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of SolarWinds Network Performance Monitor. Authentication is required to exploit this vulnerability. The specific flaw exists within the UpdateActionsDescriptions function. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://www.solarwinds.com/trust-center/security-advisories/cve-2022-36961

## Disclosure Timeline

- 2022-06-14 - Vulnerability reported to vendor
- 2022-09-30 - Coordinated public release of advisory
