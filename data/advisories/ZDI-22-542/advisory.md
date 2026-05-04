# ZDI-22-542: (0Day) Siemens Simcenter Femap NEU File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-542
- **ZDI-CAN:** ZDI-CAN-15114
- **Date:** 2022-03-28
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** Simcenter Femap
- **Credit:** xina1i
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-542/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens Simcenter Femap. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of NEU files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 09/29/21 – ZDI reported the vulnerabilities to ICS-CERT 09/29/21 – ICS-CERT acknowledged the reports 02/11/22 – ZDI requested an update 02/17/22 – ICS-CERT communicated that the cases have not been fixed 03/10/22 – ZDI requested an update 03/10/22 – ICS-CERT communicated that the cases have not been fixed 03/11/22 – ZDI notified ICS-CERT of the intention to publish the cases as 0-day advisories on 03/27/22 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-09-29 - Vulnerability reported to vendor
- 2022-03-28 - Coordinated public release of advisory
- 2022-03-29 - Advisory Updated
