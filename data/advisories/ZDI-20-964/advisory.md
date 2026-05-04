# ZDI-20-964: Delta Industrial Automation TPEditor TPE File Parsing Write-what-where Condition Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-964
- **ZDI-CAN:** ZDI-CAN-10726
- **Date:** 2020-08-10
- **CVE:** CVE-2020-16225
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Industrial Automation
- **Affected Products:** TPEditor
- **Credit:** Justin Taft (@oneupsecurity) and Chris Anastasio (@mufinnnnnnn)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-964/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Industrial Automation TPEditor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of TPE files. The issue results from the lack of proper validation of user-supplied data, which can result in a write-what-where condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Delta Industrial Automation has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-20-219-04

## Disclosure Timeline

- 2020-04-07 - Vulnerability reported to vendor
- 2020-08-10 - Coordinated public release of advisory
