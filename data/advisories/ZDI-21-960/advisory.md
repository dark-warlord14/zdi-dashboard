# ZDI-21-960: (0Day) Delta Industrial Automation DOPSoft XLS File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-960
- **ZDI-CAN:** ZDI-CAN-13127
- **Date:** 2021-08-09
- **CVE:** CVE-2021-38406
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Industrial Automation
- **Affected Products:** DOPSoft
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-960/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Industrial Automation DOPSoft. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of XLS files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

03/10/20 - ZDI reported the vulnerability to ICS-CERT 03/11/20 - ICS-CERT confirmed receipt of the report 07/12/21 - ZDI requested an update 07/23/21 - ICS-CERT requested an extension 07/23/21 - ZDI notified ICS-CERT of the intention to publish this report as a 0-day advisory on 08/03/21

## Disclosure Timeline

- 2021-03-10 - Vulnerability reported to vendor
- 2021-08-09 - Coordinated public release of advisory
