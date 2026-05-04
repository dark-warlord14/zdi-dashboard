# ZDI-23-1562: SolarWinds Access Rights Manager Incorrect Default Permissions Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1562
- **ZDI-CAN:** ZDI-CAN-21374
- **Date:** 2023-10-19
- **CVE:** CVE-2023-35183
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Access Rights Manager
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1562/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of SolarWinds Access Rights Manager. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the product installer. The issue results from incorrect permissions set on a file created by the installer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://documentation.solarwinds.com/en/success_center/arm/content/release_notes/arm_2023-2-1_release_notes.htm

## Disclosure Timeline

- 2023-06-22 - Vulnerability reported to vendor
- 2023-10-19 - Coordinated public release of advisory
