# ZDI-22-1391: PDF-XChange Editor PDF File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1391
- **ZDI-CAN:** ZDI-CAN-18892
- **Date:** 2022-10-07
- **CVE:** CVE-2022-42403
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** PDF-XChange
- **Affected Products:** PDF-XChange Editor
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1391/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of PDF-XChange Editor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PDF files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

PDF-XChange has issued an update to correct this vulnerability. More details can be found at: https://www.tracker-software.com/product/pdf-xchange-editor/history

## Disclosure Timeline

- 2022-09-20 - Vulnerability reported to vendor
- 2022-10-07 - Coordinated public release of advisory
