# ZDI-25-176: (0Day) CarlinKit CPC200-CCPA Missing Root of Trust Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-176
- **ZDI-CAN:** ZDI-CAN-25948
- **Date:** 2025-03-25
- **CVE:** CVE-2025-2762
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** CarlinKit
- **Affected Products:** CPC200-CCPA
- **Credit:** Aaron Luo and Spencer Hsieh of VicOne
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-176/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of CarlinKit CPC200-CCPA devices. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the configuration of the application system-on-chip (SoC). The issue results from the lack of a properly configured hardware root of trust. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the boot process.

## Additional Details

06/05/24 – ZDI contacted the vendor’s support team via email 07/12/24 – ZDI sent a second PSIRT contact request to CarlinKit support team 11/13/24 – ZDI asked for updates 02/18/25 – ZDI informed the vendor that since we have not received a response, we will publish the report as a 0-day advisory

## Disclosure Timeline

- 2025-03-11 - Vulnerability reported to vendor
- 2025-03-25 - Coordinated public release of advisory
- 2025-03-25 - Advisory Updated
