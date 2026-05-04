# ZDI-23-675: Delta Electronics InfraSuite Device Master Improper Access Control Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-675
- **ZDI-CAN:** ZDI-CAN-19276
- **Date:** 2023-05-17
- **CVE:** CVE-2023-1144
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** InfraSuite Device Master
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-675/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Delta Electronics InfraSuite Device Master. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the Device-Gateway service, which listens on TCP port 3100 by default. The issue results from improper access control. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-23-080-02

## Disclosure Timeline

- 2022-10-31 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
