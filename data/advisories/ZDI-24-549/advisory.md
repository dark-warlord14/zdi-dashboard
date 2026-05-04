# ZDI-24-549: Kofax Power PDF TGA File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-549
- **ZDI-CAN:** ZDI-CAN-22920
- **Date:** 2024-05-31
- **CVE:** CVE-2024-5304
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Kofax
- **Affected Products:** Power PDF
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-549/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Kofax Power PDF. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of TGA files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

docshield.tungstenautomation.com/PowerPDF/en_US/5.0.0-3uoz7ssq2b/print/ReadMe-KofaxPowerPDFAdvanced-5.0.0.18.htm

## Disclosure Timeline

- 2023-12-20 - Vulnerability reported to vendor
- 2024-05-31 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
