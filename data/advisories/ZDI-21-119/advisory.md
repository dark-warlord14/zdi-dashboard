# ZDI-21-119: Trend Micro Apex One TmCCSF Out-Of-Bounds Write Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-119
- **ZDI-CAN:** ZDI-CAN-11896
- **Date:** 2021-01-29
- **CVE:** CVE-2021-25249
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Lynn
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-119/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Apex One. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within TmCCSF.exe. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000284202

## Disclosure Timeline

- 2020-09-30 - Vulnerability reported to vendor
- 2021-01-29 - Coordinated public release of advisory
