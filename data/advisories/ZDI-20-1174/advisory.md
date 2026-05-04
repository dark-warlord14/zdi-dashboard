# ZDI-20-1174: (0Day) Fatek Automation PLC WinProladder TAB File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1174
- **ZDI-CAN:** ZDI-CAN-10146
- **Date:** 2020-09-14
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fatek Automation
- **Affected Products:** PLC WinProladder
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1174/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fatek Automation PLC WinProladder. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of TAB files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 04/07/20 – ZDI reported the vulnerability to ICS-CERT 04/17/20 – ICS-CERT acknowledged the report 08/17/20 – ZDI requested an update 08/20/20 – ICS-CERT indicated there had been no response from the vendor despite multiple requests 08/20/20 – ZDI notified ICS-CERT of the intention to publish the report as a 0-day advisory 09/04/20 – ZDI notified ICS-CERT of the intention to publish the report as a 0-day advisory on 09/10/20 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-04-07 - Vulnerability reported to vendor
- 2020-09-14 - Coordinated public release of advisory
