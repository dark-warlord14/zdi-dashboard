# ZDI-20-1095: Trend Micro Apex One Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1095
- **ZDI-CAN:** ZDI-CAN-10760
- **Date:** 2020-08-31
- **CVE:** CVE-2020-24558
- **CVSS:** 2.5
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** @Kharosx0
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1095/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Trend Micro Apex One. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within OfcPIPC_64x.dll. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000263632

## Disclosure Timeline

- 2020-03-31 - Vulnerability reported to vendor
- 2020-08-31 - Coordinated public release of advisory
