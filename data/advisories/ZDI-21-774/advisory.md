# ZDI-21-774: Trend Micro Password Manager Exposed Dangerous Function Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-774
- **ZDI-CAN:** ZDI-CAN-13363
- **Date:** 2021-07-05
- **CVE:** CVE-2021-32462
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Password Manager
- **Credit:** Simon Zuckerbraun - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-774/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Trend Micro Password Manager. Authentication is required to exploit this vulnerability. The specific flaw exists within the Trend Micro Password Manager Central Control Service. The issue results from the exposure of a dangerous method or function to unprivileged users. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/TMKA-10388

## Disclosure Timeline

- 2021-03-17 - Vulnerability reported to vendor
- 2021-07-05 - Coordinated public release of advisory
