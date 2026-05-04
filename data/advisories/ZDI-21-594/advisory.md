# ZDI-21-594: (0Day) Microsoft Windows JET Database Engine Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-594
- **ZDI-CAN:** ZDI-CAN-12334
- **Date:** 2021-05-18
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Hossein Lotfi of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-594/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the JET database engine. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 11/13/20 – ZDI reported the vulnerability to the vendor 11/13/20 – The vendor acknowledged the report 03/31/21 – ZDI requested an update 03/31/21 – The vendor indicated they were working on a fix scheduled for April release 04/26/21 – ZDI requested an update and notified the vendor of the intention to publish the report as a 0-day advisory 05/03/21 – ZDI requested an update 05/07/21 – The vendor indicated they would not issue a fix 05/11/21 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory on 05/18/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-11-13 - Vulnerability reported to vendor
- 2021-05-18 - Coordinated public release of advisory
