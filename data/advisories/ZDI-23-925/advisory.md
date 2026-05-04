# ZDI-23-925: Kofax Power PDF exportAsText Exposed Dangerous Method Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-925
- **ZDI-CAN:** ZDI-CAN-20230
- **Date:** 2023-07-13
- **CVE:** CVE-2023-37330
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Kofax
- **Affected Products:** Power PDF
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-925/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Kofax Power PDF. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the exportAsText method. The application exposes a JavaScript interface that allows the attacker to write arbitrary files. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Fixed in Power PDF 5.0 Standard & Advanced in v5.0.0.10.0.23307. https://docshield.kofax.com/PowerPDF/en_US/5.0.0-3uoz7ssq2b/print/ReadMe-KofaxPowerPDF-5.0.0.10_EN.htm

## Disclosure Timeline

- 2023-02-27 - Vulnerability reported to vendor
- 2023-07-13 - Coordinated public release of advisory
