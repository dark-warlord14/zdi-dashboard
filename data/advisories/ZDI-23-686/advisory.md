# ZDI-23-686: Delta Electronics InfraSuite Device Master Incorrect Permission Assignment Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-686
- **ZDI-CAN:** ZDI-CAN-19590
- **Date:** 2023-05-17
- **CVE:** CVE-2023-1135
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** InfraSuite Device Master
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-686/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Delta Electronics InfraSuite Device Master. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the product installer. The product sets incorrect permissions on folders. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-23-080-02

## Disclosure Timeline

- 2022-11-30 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
