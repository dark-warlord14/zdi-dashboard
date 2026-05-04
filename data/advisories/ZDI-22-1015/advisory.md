# ZDI-22-1015: ABB Automation Builder Platform Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1015
- **ZDI-CAN:** ZDI-CAN-16321
- **Date:** 2022-07-15
- **CVE:** CVE-2022-31219
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** ABB
- **Affected Products:** Automation Builder Platform
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1015/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of ABB Automation Builder Platform. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Drive Composer installer. By creating a symbolic link, an attacker can abuse the installer to create a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

ABB has issued an update to correct this vulnerability. More details can be found at: https://library.e.abb.com/public/0bc9ed3188ff43be94f2cbdc1751a72d/Vulnerabilities_in_Automation_Builder_and_Drive_Composer_and_Mint_WorkBench.pdf?x-sign=Dsvwu1eOxEWGDKECZJMzhUkv4wylDwof6PtNKvY8QFk+nBjFCRKlgeR096xY5FkJ

## Disclosure Timeline

- 2022-01-26 - Vulnerability reported to vendor
- 2022-07-15 - Coordinated public release of advisory
