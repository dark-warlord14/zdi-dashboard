# ZDI-25-986: Autodesk On-Demand Install Services adsk_IPCUpdaterChannel Origin Validation Error Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-986
- **ZDI-CAN:** ZDI-CAN-27900
- **Date:** 2025-11-10
- **CVE:** CVE-2025-10885
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Autodesk
- **Affected Products:** On-Demand Install Services
- **Credit:** Masahiro Iida with LAC Co., Ltd. https://www.lac.co.jp/
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-986/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Autodesk On-Demand Install Services. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the AdskAccessServiceHost service. The issue results from insufficient validation of the origin of commands. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Autodesk has issued an update to correct this vulnerability. More details can be found at: https://www.autodesk.com/trust/security-advisories/adsk-sa-2025-0022

## Disclosure Timeline

- 2025-09-11 - Vulnerability reported to vendor
- 2025-11-10 - Coordinated public release of advisory
- 2025-11-10 - Advisory Updated
