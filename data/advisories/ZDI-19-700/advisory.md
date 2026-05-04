# ZDI-19-700: (0Day) EZAutomation EZTouch Editor EZP File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-700
- **ZDI-CAN:** ZDI-CAN-7890
- **Date:** 2019-08-12
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** EZAutomation
- **Affected Products:** EZTouch Editor
- **Credit:** 9sg Security Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-700/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of EZAutomation EZTouch Editor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of EZP files. When parsing the file, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 03/08/2019 – ZDI reported the vulnerability to ICS-CERT 03/12/2019 – ICS-CERT acknowledged the report 07/05/2019 – ZDI requested an update 07/08/2019 – ICS-CERT indicated the vendor was working towards a fix but communication was limited 07/17/2019 – ICS-CERT indicated they had received a contact from the vendor and the fix is coming within a month 07/18/2019 – ZDI asked if the fix could be pushed up to the end of the month 07/22/2019 – ZDI indicated the intention to publish the report as 0-day on 08/12/2019 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2019-03-08 - Vulnerability reported to vendor
- 2019-08-12 - Coordinated public release of advisory
