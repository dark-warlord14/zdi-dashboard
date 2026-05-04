# ZDI-21-773: Trend Micro Password Manager Integer Truncation Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-773
- **ZDI-CAN:** ZDI-CAN-13319
- **Date:** 2021-07-05
- **CVE:** CVE-2021-32461
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Password Manager
- **Credit:** Simon Zuckerbraun - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-773/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Password Manager. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Trend Micro Password Manager Central Control Service. The issue results from the lack of proper validation of user-supplied data, which can result in an integer truncation before allocating a buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/TMKA-10388

## Disclosure Timeline

- 2021-03-03 - Vulnerability reported to vendor
- 2021-07-05 - Coordinated public release of advisory
