# ZDI-18-559: Samsung Galaxy Apps Activity Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-559
- **ZDI-CAN:** ZDI-CAN-5331
- **Date:** 2018-06-07
- **CVE:** CVE-2018-10500
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Samsung
- **Affected Products:** Galaxy Apps
- **Credit:** Tencent Keen Security Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-559/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Samsung Galaxy Apps. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of push messages. The issue lies in the ability to start an activity with controlled arguments. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the application.

## Additional Details

Patched with ThemeStore v. 4.0.60.80109 and GalaxyApps v. 6.4.0.15

## Disclosure Timeline

- 2017-11-05 - Vulnerability reported to vendor
- 2018-06-07 - Coordinated public release of advisory
- 2018-06-07 - Advisory Updated
