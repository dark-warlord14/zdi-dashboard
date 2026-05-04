# ZDI-24-1679: Tungsten Automation Power PDF JP2 File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1679
- **ZDI-CAN:** ZDI-CAN-25565
- **Date:** 2024-12-11
- **CVE:** CVE-2024-12549
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Tungsten Automation
- **Affected Products:** Power PDF
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1679/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Tungsten Automation Power PDF. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of JP2 files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

docshield.tungstenautomation.com/PowerPDF/en_US/5.1.1-x2ki7a3ycc/print/ReadMe-TungstenPowerPDFBusiness-5.1.1.2.htm

## Disclosure Timeline

- 2024-10-31 - Vulnerability reported to vendor
- 2024-12-11 - Coordinated public release of advisory
- 2024-12-11 - Advisory Updated
