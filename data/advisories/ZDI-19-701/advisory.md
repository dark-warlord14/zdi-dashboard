# ZDI-19-701: (0Day) EZAutomation EZPLC EZC File Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-701
- **ZDI-CAN:** ZDI-CAN-8028
- **Date:** 2019-08-12
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** EZAutomation
- **Affected Products:** EZPLC
- **Credit:** 9sg Security Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-701/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of EZAutomation EZPLC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of EZC files. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 03/27/2019 – ZDI reported the vulnerability to ICS-CERT 04/01/2019 – ICS-CERT acknowledged the report 07/17/2019 – ICS-CERT indicated they had received a contact from the vendor and the fix is coming within a month 07/18/2019 – ZDI asked if the fix could be pushed up to the end of the month 07/22/2019 – ZDI indicated the intention to publish the report as 0-day on 08/12/2019 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2019-03-27 - Vulnerability reported to vendor
- 2019-08-12 - Coordinated public release of advisory
