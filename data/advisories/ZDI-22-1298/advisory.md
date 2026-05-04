# ZDI-22-1298: Trend Micro Deep Security Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1298
- **ZDI-CAN:** ZDI-CAN-16595
- **Date:** 2022-09-23
- **CVE:** CVE-2022-40708
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:L
- **Affected Vendors:** Trend Micro
- **Affected Products:** Deep Security
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1298/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Trend Micro Deep Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the User Mode Hooking Monitor Engine. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000291590

## Disclosure Timeline

- 2022-02-16 - Vulnerability reported to vendor
- 2022-09-23 - Coordinated public release of advisory
