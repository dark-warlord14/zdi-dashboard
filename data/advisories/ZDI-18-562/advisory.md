# ZDI-18-562: (Pwn2Own) Samsung Members Intent Proxy Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-562
- **ZDI-CAN:** ZDI-CAN-5361
- **Date:** 2018-06-07
- **CVE:** CVE-2018-11614
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Samsung
- **Affected Products:** Members
- **Credit:** MWR Labs - Alex Plaskett James Loureiro Robert Miller and Georgi Geshev
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-562/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on vulnerable installations of Samsung Members. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of Intents. The issue lies in the ability to send an Intent that would not otherwise be reachable. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the application.

## Additional Details

Patched with Samsung Members v. 2.4.25

## Disclosure Timeline

- 2017-11-05 - Vulnerability reported to vendor
- 2018-06-07 - Coordinated public release of advisory
- 2018-06-07 - Advisory Updated
