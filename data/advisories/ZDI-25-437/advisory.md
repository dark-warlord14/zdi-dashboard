# ZDI-25-437: PDF-XChange Editor PRC File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-437
- **ZDI-CAN:** ZDI-CAN-26724
- **Date:** 2025-06-25
- **CVE:** CVE-2025-6652
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** PDF-XChange
- **Affected Products:** PDF-XChange Editor
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-437/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of PDF-XChange Editor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PRC files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

PDF-XChange has issued an update to correct this vulnerability. More details can be found at: https://www.pdf-xchange.com/support/security-bulletins.html

## Disclosure Timeline

- 2025-03-21 - Vulnerability reported to vendor
- 2025-06-25 - Coordinated public release of advisory
- 2025-06-25 - Advisory Updated
