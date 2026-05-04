# ZDI-18-422: (0Day) Delta Industrial Automation DOPSoft DPA File TagTotalSize Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-422
- **ZDI-CAN:** ZDI-CAN-5273
- **Date:** 2018-05-14
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Delta Industrial Automation
- **Affected Products:** DOPSoft
- **Credit:** Ghirmay Desta
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-422/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Delta Industrial Automation DOPSoft. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of the TagTotalSize attribute in a DPA file. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 10/10/17 - ZDI sent the vulnerability report to ICS-CERT 03/26/18 - ZDI sent a follow-up inquiry about the report 04/20/18 - ZDI sent a follow-up inquiry about the report and notified of the intent to 0-day on 5/3/2018 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2017-10-10 - Vulnerability reported to vendor
- 2018-05-14 - Coordinated public release of advisory
- 2018-05-14 - Advisory Updated
