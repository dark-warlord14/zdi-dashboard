# ZDI-23-771: (0Day) Fatek Automation FvDesigner FPJ File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-771
- **ZDI-CAN:** ZDI-CAN-18183
- **Date:** 2023-05-31
- **CVE:** CVE-2023-34273
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fatek Automation
- **Affected Products:** FvDesigner
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-771/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fatek Automation FvDesigner. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of FPJ files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

08/26/22 – ZDI reported the vulnerability to the vendor. 08/29/22 – The vendor acknowledged the report. 05/12/23 – ZDI inquired about an email regarding a possible patch from November of 2022, but we were informed by the vendor that we were copied by mistake. 05/15/23 – ZDI asked for an update. 05/24/23 – The ZDI informed the vendor that the case will be published as a zero-day advisory on 05/31/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2022-08-26 - Vulnerability reported to vendor
- 2023-05-31 - Coordinated public release of advisory
