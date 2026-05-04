# ZDI-23-1906: (0Day) Kofax Power PDF U3D File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1906
- **ZDI-CAN:** ZDI-CAN-21755
- **Date:** 2023-12-21
- **CVE:** CVE-2023-51597
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Kofax
- **Affected Products:** Power PDF
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1906/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Kofax Power PDF. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of U3D files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

07/20/23 – ZDI reported the vulnerabilities to the vendor 07/20/23 – The vendor acknowledged the reports 07/28/23 – The vendor confirmed the issues 12/15/23 – The vendor communicated that the cases would be fixed in Q2 2024 12/15/23 – ZDI notified the vendor of the intention to publish the cases as 0-day advisories -- Mitigation: On Mar 27, 2024, the vendor released Power PDF Advanced 5.0.0 Fix Pack 19 https://docshield.tungstenautomation.com/PowerPDF/en_US/5.0.0-3uoz7ssq2b/print/ReadMe-KofaxPowerPDFAdvanced-5.0.0.19.htm

## Disclosure Timeline

- 2023-07-20 - Vulnerability reported to vendor
- 2023-12-21 - Coordinated public release of advisory
- 2024-06-06 - Advisory Updated
