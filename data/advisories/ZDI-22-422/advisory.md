# ZDI-22-422: (0Day) Delta Industrial Automation CNCSoft ScreenEditor DPB File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-422
- **ZDI-CAN:** ZDI-CAN-15202
- **Date:** 2022-03-01
- **CVE:** CVE-2022-1404
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Industrial Automation
- **Affected Products:** CNCSoft ScreenEditor
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-422/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Industrial Automation CNCSoft ScreenEditor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DPB files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of Administrator.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 10/15/21 – ZDI reported the vulnerability to the vendor 01/12/22 – ZDI requested an update 02/18/22 – ZDI notified the vendor of the intention to publish the cases as 0-day advisories on 02/28/22 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-10-15 - Vulnerability reported to vendor
- 2022-03-01 - Coordinated public release of advisory
- 2022-05-10 - Advisory Updated
