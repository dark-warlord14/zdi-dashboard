# ZDI-24-1189: (0Day) Visteon Infotainment App SoC Missing Immutable Root of Trust in Hardware Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1189
- **ZDI-CAN:** ZDI-CAN-23759
- **Date:** 2024-08-30
- **CVE:** CVE-2024-8357
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Visteon
- **Affected Products:** Infotainment
- **Credit:** Dmitry "InfoSecDJ" Janushkevich of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1189/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Visteon Infotainment systems. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the configuration of the application system-on-chip (SoC). The issue results from the lack of properly configured hardware root of trust. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the boot process.

## Additional Details

04/24/24 – ZDI reported the vulnerabilities to the vendor 04/30/24 – ZDI asked for updates 07/29/24 – ZDI asked for updates 08/16/24 – ZDI notified the vendor of the intention to publish the cases as 0-day advisories on 08/30/24 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application

## Disclosure Timeline

- 2024-04-24 - Vulnerability reported to vendor
- 2024-08-30 - Coordinated public release of advisory
- 2024-08-30 - Advisory Updated
