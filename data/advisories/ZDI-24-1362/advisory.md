# ZDI-24-1362: Tungsten Automation Power PDF PDF File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1362
- **ZDI-CAN:** ZDI-CAN-24480
- **Date:** 2024-10-11
- **CVE:** CVE-2024-9764
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Tungsten Automation
- **Affected Products:** Power PDF
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1362/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Tungsten Automation Power PDF. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PDF files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in version 5.1 which is available in the Tungsten Download Center ( https://esd.tungstenautomation.com/Registrations/ChooseLanguage )

## Disclosure Timeline

- 2024-06-13 - Vulnerability reported to vendor
- 2024-10-11 - Coordinated public release of advisory
- 2024-10-11 - Advisory Updated
