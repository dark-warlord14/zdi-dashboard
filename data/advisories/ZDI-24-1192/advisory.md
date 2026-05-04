# ZDI-24-1192: (0Day) Visteon Infotainment REFLASH_DDU_ExtractFile Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1192
- **ZDI-CAN:** ZDI-CAN-23421
- **Date:** 2024-08-30
- **CVE:** CVE-2024-8360
- **CVSS:** 6.8
- **CVSS Vector:** AV:P/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Visteon
- **Affected Products:** Infotainment
- **Credit:** Dmitry "InfoSecDJ" Janushkevich of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1192/
## Vulnerability Details

This vulnerability allows physically present attackers to execute arbitrary code on affected installations of Visteon Infotainment systems. Authentication is not required to exploit this vulnerability. The specific flaw exists within the REFLASH_DDU_ExtractFile function. A crafted software update file can trigger execution of a system call composed from a user-supplied string. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

04/24/24 – ZDI reported the vulnerabilities to the vendor 04/30/24 – ZDI asked for updates 07/29/24 – ZDI asked for updates 08/16/24 – ZDI notified the vendor of the intention to publish the cases as 0-day advisories on 08/30/24 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application

## Disclosure Timeline

- 2024-04-24 - Vulnerability reported to vendor
- 2024-08-30 - Coordinated public release of advisory
- 2024-08-30 - Advisory Updated
