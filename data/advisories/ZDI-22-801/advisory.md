# ZDI-22-801: Trend Micro Internet Security Exposed Dangerous Method Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-801
- **ZDI-CAN:** ZDI-CAN-15757
- **Date:** 2022-05-27
- **CVE:** CVE-2022-30703
- **CVSS:** 6.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** Internet Security
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-801/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Trend Micro Internet Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the NCIE Scanner module. The module exposes a dangerous function to unprivileged users. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the kernel.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/tmka-11021

## Disclosure Timeline

- 2022-01-07 - Vulnerability reported to vendor
- 2022-05-27 - Coordinated public release of advisory
