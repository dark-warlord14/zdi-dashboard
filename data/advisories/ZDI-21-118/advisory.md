# ZDI-21-118: Trend Micro Apex One Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-118
- **ZDI-CAN:** ZDI-CAN-11895
- **Date:** 2021-01-29
- **CVE:** CVE-2021-25248
- **CVSS:** 2.5
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Lynn and Jay Lo
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-118/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Trend Micro Apex One. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within TmCCSF.exe. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000284202

## Disclosure Timeline

- 2020-09-23 - Vulnerability reported to vendor
- 2021-01-29 - Coordinated public release of advisory
