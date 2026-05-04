# ZDI-25-585: Trend Micro Maximum Security Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-585
- **ZDI-CAN:** ZDI-CAN-26887
- **Date:** 2025-07-08
- **CVE:** CVE-2025-52521
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Maximum Security
- **Credit:** Simon Zuckerbraun of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-585/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Maximum Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Regain Disk Space functionality. By creating a junction, an attacker can abuse the Platinum Host Service to delete arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/tmka-18876

## Disclosure Timeline

- 2025-04-04 - Vulnerability reported to vendor
- 2025-07-08 - Coordinated public release of advisory
- 2025-07-08 - Advisory Updated
