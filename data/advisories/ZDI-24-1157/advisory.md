# ZDI-24-1157: Rockwell Automation ThinManager ThinServer Arbitrary File Creation Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1157
- **ZDI-CAN:** ZDI-CAN-24006
- **Date:** 2024-08-22
- **CVE:** CVE-2024-7987
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Rockwell Automation
- **Affected Products:** ThinManager
- **Credit:** Nicholas Zubrisky (@NZubrisky) of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1157/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Rockwell Automation ThinManager. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the ThinServer service which listens on TCP port 2031 by default. The issue results from the lack of proper access controls set on resources used by the service. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Rockwell Automation has issued an update to correct this vulnerability. More details can be found at: https://www.rockwellautomation.com/en-ca/trust-center/security-advisories/advisory.SD1692.html

## Disclosure Timeline

- 2024-04-24 - Vulnerability reported to vendor
- 2024-08-22 - Coordinated public release of advisory
- 2024-08-22 - Advisory Updated
