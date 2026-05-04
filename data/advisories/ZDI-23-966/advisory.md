# ZDI-23-966: Kofax Power PDF importDataObject Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-966
- **ZDI-CAN:** ZDI-CAN-20603
- **Date:** 2023-07-13
- **CVE:** CVE-2023-38092
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Kofax
- **Affected Products:** Power PDF
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-966/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Kofax Power PDF. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the importDataObject method. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in Power PDF 5.0 Standard & Advanced in v5.0.0.10.0.23307. https://docshield.kofax.com/PowerPDF/en_US/5.0.0-3uoz7ssq2b/print/ReadMe-KofaxPowerPDF-5.0.0.10_EN.htm

## Disclosure Timeline

- 2023-05-19 - Vulnerability reported to vendor
- 2023-07-13 - Coordinated public release of advisory
