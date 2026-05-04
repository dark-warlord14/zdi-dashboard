# ZDI-23-1910: (0Day) Kofax Power PDF JP2 File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1910
- **ZDI-CAN:** ZDI-CAN-21834
- **Date:** 2024-06-06
- **CVE:** CVE-2023-51609
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Kofax
- **Affected Products:** Power PDF
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1910/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Kofax Power PDF. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of JP2 files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

08/02/23 – ZDI reported the vulnerabilities to the vendor 08/02/23 – The vendor acknowledged the reports 08/04/23 – The vendor confirmed the issues 12/12/23 – ZDI requested an update 12/15/23 – The vendor communicated that the cases would be fixed in Q2 2024 12/15/23 – ZDI notified the vendor of the intention to publish the cases as 0-day advisories -- Mitigation: Fixed in KofaxPowerPDFAdvanced-5.0.0.21 https://docshield.tungstenautomation.com/PowerPDF/en_US/5.0.0-3uoz7ssq2b/print/ReadMe-KofaxPowerPDFAdvanced-5.0.0.21.htm

## Disclosure Timeline

- 2023-08-02 - Vulnerability reported to vendor
- 2024-06-06 - Coordinated public release of advisory
- 2024-06-06 - Advisory Updated
