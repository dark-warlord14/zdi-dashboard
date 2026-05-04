# ZDI-23-639: Schneider Electric APC Easy UPS Online Incorrect Permission Assignment Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-639
- **ZDI-CAN:** ZDI-CAN-17649
- **Date:** 2023-05-17
- **CVE:** CVE-2022-42972
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** APC Easy
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-639/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Schneider Electric APC Easy UPS Online. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the product installer. The product sets incorrect permissions on folders. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-22-347-02

## Disclosure Timeline

- 2022-06-17 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
