# ZDI-21-1604: SolarWinds Network Performance Monitor SendSyslog Exposed Dangerous Function Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1604
- **ZDI-CAN:** ZDI-CAN-14859
- **Date:** 2021-12-23
- **CVE:** CVE-2021-35234
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Network Performance Monitor
- **Credit:** @fkadibs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1604/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of SolarWinds Network Performance Monitor. Authentication is required to exploit this vulnerability. The specific flaw exists within the SendSyslog class. This class allows a crafted user-supplied string to be processed as an SQL statement. An attacker can leverage this vulnerability to escalate privileges to the level of an application administrator.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://www.solarwinds.com/trust-center/security-advisories/cve-2021-35234

## Disclosure Timeline

- 2021-10-01 - Vulnerability reported to vendor
- 2021-12-23 - Coordinated public release of advisory
