# ZDI-18-560: (Pwn2Own) Samsung Galaxy Apps Staging Mode Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-560
- **ZDI-CAN:** ZDI-CAN-5359
- **Date:** 2018-06-07
- **CVE:** CVE-2018-10502
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Samsung
- **Affected Products:** Galaxy Apps
- **Credit:** MWR Labs - Alex Plaskett James Loureiro Robert Miller and Georgi Geshev
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-560/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Samsung Galaxy Apps. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of a staging mode. The issue lies in the ability to change the configuration based on the presence of a file in an user-controlled location. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the application.

## Additional Details

Patched with GalaxyApps v. 4.2.18.2

## Disclosure Timeline

- 2017-11-05 - Vulnerability reported to vendor
- 2018-06-07 - Coordinated public release of advisory
- 2018-06-07 - Advisory Updated
