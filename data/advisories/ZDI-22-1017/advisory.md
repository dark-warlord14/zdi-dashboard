# ZDI-22-1017: (Pwn2Own) Inductive Automation Ignition Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1017
- **ZDI-CAN:** ZDI-CAN-17265
- **Date:** 2022-07-15
- **CVE:** CVE-2022-35870
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Inductive Automation
- **Affected Products:** Ignition
- **Credit:** @_s_n_t of @pentestltd
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1017/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Inductive Automation Ignition. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within com.inductiveautomation.metro.impl. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Inductive Automation has issued an update to correct this vulnerability. More details can be found at: https://support.inductiveautomation.com/hc/en-us/articles/7625759776653-Regarding-Pwn2Own-2022-Vulnerabilities

## Disclosure Timeline

- 2022-05-09 - Vulnerability reported to vendor
- 2022-07-15 - Coordinated public release of advisory
