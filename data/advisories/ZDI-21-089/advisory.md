# ZDI-21-089: (0Day) Microsoft Windows PowerShell Shell Handler Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-089
- **ZDI-CAN:** ZDI-CAN-12565
- **Date:** 2021-01-27
- **CVE:** N/A
- **CVSS:** 6.4
- **CVSS Vector:** AV:N/AC:H/PR:H/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** CSZQ
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-089/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the shell handler for opening a folder in PowerShell. Crafted data in a folder name can trigger execution of a system call composed from a user-supplied string. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 12/23/20 – ZDI reported the vulnerability to the vendor 12/23/20 – The vendor acknowledged the report 12/28/20 – The vendor confirmed the behavior of the report 12/28/20 – The vendor indicated the case does not meet the bar for servicing 01/19/21 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory on 01/27/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-12-23 - Vulnerability reported to vendor
- 2021-01-27 - Coordinated public release of advisory
