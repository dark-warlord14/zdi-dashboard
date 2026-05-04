# ZDI-25-365: Trend Micro Apex One Security Agent ntrmv Uncontrolled Search Path Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-365
- **ZDI-CAN:** ZDI-CAN-25771
- **Date:** 2025-06-11
- **CVE:** CVE-2025-49158
- **CVSS:** 6.7
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Vladislav Berghici of Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-365/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Apex One Security Agent. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. Furthermore, privilege escalation occurs only if an administrator uninstalls the Security Agent from the affected computer. The specific flaw exists within the product uninstaller. The product executes a program from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/en-US/solution/KA-0019917

## Disclosure Timeline

- 2024-12-06 - Vulnerability reported to vendor
- 2025-06-11 - Coordinated public release of advisory
- 2025-06-11 - Advisory Updated
