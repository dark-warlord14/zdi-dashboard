# ZDI-20-975: Marvell QConvergeConsole Exposed Dangerous Method or Function Remote Code Execution

## Metadata

- **ZDI ID:** ZDI-20-975
- **ZDI-CAN:** ZDI-CAN-10799
- **Date:** 2020-08-10
- **CVE:** CVE-2020-17388
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Marvell
- **Affected Products:** QConvergeConsole
- **Credit:** Sivathmican Sivakumaran of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-975/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Marvell QConvergeConsole. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the Tomcat configuration file. The issue results from the lack of proper restriction to the Tomcat admin console. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Marvell has issued an update to correct this vulnerability. More details can be found at: https://www.marvell.com/content/dam/marvell/en/public-collateral/fibre-channel/marvell-fibre-channel-security-advisory-2020-07.pdf

## Disclosure Timeline

- 2020-04-01 - Vulnerability reported to vendor
- 2020-08-10 - Coordinated public release of advisory
