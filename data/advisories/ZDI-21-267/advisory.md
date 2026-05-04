# ZDI-21-267: (0Day) Fatek Automation PLC WinProladder PWD File Parsing Integer Underflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-267
- **ZDI-CAN:** ZDI-CAN-12001
- **Date:** 2021-03-11
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fatek Automation
- **Affected Products:** PLC WinProladder
- **Credit:** Francis Provencher {PRL}
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-267/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fatek Automation PLC WinProladder. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PWD files. The issue results from the lack of proper validation of user-supplied data, which can result in an integer underflow before writing to memory. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 11/24/20 – ZDI reported the vulnerability to ICS-CERT 02/08/21 – ICS-CERT indicated the vendor had been unresponsive and provided an advisory draft to publish on 03/11/21 02/11/21 – ZDI agreed with ICS-CERT to publish the report as a 0-day advisory 03/11/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-11-24 - Vulnerability reported to vendor
- 2021-03-11 - Coordinated public release of advisory
