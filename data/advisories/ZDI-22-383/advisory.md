# ZDI-22-383: Microsoft Office Excel XLS File Parsing Untrusted Pointer Dereference Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-383
- **ZDI-CAN:** ZDI-CAN-15585
- **Date:** 2022-02-18
- **CVE:** CVE-2022-22716
- **CVSS:** 2.5
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** Jaanus Kääp, Clarified Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-383/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Microsoft Office Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of XLS files. The issue results from the lack of proper validation of a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-22716

## Disclosure Timeline

- 2021-10-27 - Vulnerability reported to vendor
- 2022-02-18 - Coordinated public release of advisory
