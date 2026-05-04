# ZDI-24-219: Kofax Power PDF app response Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-219
- **ZDI-CAN:** ZDI-CAN-22588
- **Date:** 2024-03-01
- **CVE:** CVE-2024-27338
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Kofax
- **Affected Products:** Power PDF
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-219/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Kofax Power PDF. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the app.response method. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

docshield.kofax.com/PowerPDF/en_US/5.0.0-3uoz7ssq2b/print/ReadMe-KofaxPowerPDFAdvanced-5.0.0.17.htm

## Disclosure Timeline

- 2023-11-16 - Vulnerability reported to vendor
- 2024-03-01 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
