# ZDI-23-092: RARLAB WinRAR ZIP File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-092
- **ZDI-CAN:** ZDI-CAN-19232
- **Date:** 2023-01-20
- **CVE:** CVE-2022-43650
- **CVSS:** 2.5
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** RARLAB
- **Affected Products:** WinRAR
- **Credit:** Bakker
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-092/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of RARLAB WinRAR. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of ZIP files. Crafted data in a ZIP file can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

RARLAB has issued an update to correct this vulnerability. More details can be found at: https://www.win-rar.com/singlenewsview.html?&L=0&tx_ttnews%5Btt_news%5D=216&cHash=983dfbcc83fb1b64a5f792891a281709

## Disclosure Timeline

- 2022-11-21 - Vulnerability reported to vendor
- 2023-01-20 - Coordinated public release of advisory
