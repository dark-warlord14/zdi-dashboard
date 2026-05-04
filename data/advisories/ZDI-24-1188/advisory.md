# ZDI-24-1188: (0Day) Visteon Infotainment VIP MCU Code Insufficient Validation of Data Authenticity Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1188
- **ZDI-CAN:** ZDI-CAN-23758
- **Date:** 2024-08-30
- **CVE:** CVE-2024-8356
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Visteon
- **Affected Products:** Infotainment
- **Credit:** Dmitry "InfoSecDJ" Janushkevich of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1188/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Visteon Infotainment systems. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the firmware update process of the VIP microcontroller. The process does not properly verify authenticity of the supplied firmware image before programming it into internal memory. An attacker can leverage this vulnerability to escalate privileges execute arbitrary code in the context of the VIP MCU.

## Additional Details

04/24/24 – ZDI reported the vulnerabilities to the vendor 04/30/24 – ZDI asked for updates 07/29/24 – ZDI asked for updates 08/16/24 – ZDI notified the vendor of the intention to publish the cases as 0-day advisories on 08/30/24 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application

## Disclosure Timeline

- 2024-04-24 - Vulnerability reported to vendor
- 2024-08-30 - Coordinated public release of advisory
- 2024-08-30 - Advisory Updated
