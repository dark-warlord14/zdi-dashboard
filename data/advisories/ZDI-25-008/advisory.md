# ZDI-25-008: Trend Micro Deep Security Agent Incorrect Permissions Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-008
- **ZDI-CAN:** ZDI-CAN-24932
- **Date:** 2025-01-08
- **CVE:** CVE-2024-55955
- **CVSS:** 6.7
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Deep Security
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-008/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Deep Security Agent. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. Subsequent user interaction on the part of an administrator is additionally required. The specific flaw exists within the agent installer. The issue results from incorrect permissions set on a product folder created by the installer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of an administrator at medium integrity.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/en-US/solution/KA-0018571

## Disclosure Timeline

- 2024-08-22 - Vulnerability reported to vendor
- 2025-01-08 - Coordinated public release of advisory
- 2025-01-08 - Advisory Updated
