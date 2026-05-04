# ZDI-23-905: Delta Electronics InfraSuite Device Master modifyusergroup Improper Access Control Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-905
- **ZDI-CAN:** ZDI-CAN-20911
- **Date:** 2023-07-10
- **CVE:** CVE-2023-30765
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** InfraSuite Device Master
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-905/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Delta Electronics InfraSuite Device Master. Authentication is required to exploit this vulnerability. The specific flaw exists within the modifyusergroup endpoint. The issue results from improper access control. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-23-180-01

## Disclosure Timeline

- 2023-05-03 - Vulnerability reported to vendor
- 2023-07-10 - Coordinated public release of advisory
