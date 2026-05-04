# ZDI-24-1355: Tungsten Automation Power PDF PDF File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1355
- **ZDI-CAN:** ZDI-CAN-24471
- **Date:** 2024-10-11
- **CVE:** CVE-2024-9754
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Tungsten Automation
- **Affected Products:** Power PDF
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1355/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Tungsten Automation Power PDF. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PDF files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Fixed in version 5.1 which is available in the Tungsten Download Center ( https://esd.tungstenautomation.com/Registrations/ChooseLanguage )

## Disclosure Timeline

- 2024-06-13 - Vulnerability reported to vendor
- 2024-10-11 - Coordinated public release of advisory
- 2024-10-11 - Advisory Updated
