# ZDI-21-1243: SolarWinds Orion Network Performance Monitor DisableNOCView SQL Injection Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1243
- **ZDI-CAN:** ZDI-CAN-13460
- **Date:** 2021-10-28
- **CVE:** CVE-2021-35212
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Orion Network Performance Monitor
- **Credit:** Piotr Bazydlo (@chudypb)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1243/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of SolarWinds Orion Network Performance Monitor. Authentication is required to exploit this vulnerability. The specific flaw exists within the DisableNOCView method. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to escalate privileges to the level of an administrator.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://www.solarwinds.com/trust-center/security-advisories/cve-2021-35212

## Disclosure Timeline

- 2021-04-30 - Vulnerability reported to vendor
- 2021-10-28 - Coordinated public release of advisory
- 2022-05-26 - Advisory Updated
