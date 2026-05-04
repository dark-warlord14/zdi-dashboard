# ZDI-24-1156: Rockwell Automation ThinManager ThinServer Arbitrary File Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1156
- **ZDI-CAN:** ZDI-CAN-24002
- **Date:** 2024-08-22
- **CVE:** CVE-2024-7986
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Rockwell Automation
- **Affected Products:** ThinManager
- **Credit:** Nicholas Zubrisky (@NZubrisky) of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1156/
## Vulnerability Details

This vulnerability allows local attackers to read arbitrary files on affected installations of Rockwell Automation ThinManager. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the ThinServer service which listens on TCP port 8443 by default. The issue results from the lack of proper access controls set on resources used by the service. An attacker can leverage this vulnerability to read files in the context of the SYSTEM.

## Additional Details

Rockwell Automation has issued an update to correct this vulnerability. More details can be found at: https://www.rockwellautomation.com/en-ca/trust-center/security-advisories/advisory.SD1692.html

## Disclosure Timeline

- 2024-04-24 - Vulnerability reported to vendor
- 2024-08-22 - Coordinated public release of advisory
- 2024-08-22 - Advisory Updated
