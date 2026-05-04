# ZDI-22-1093: PDF-XChange Editor saveAs Exposed Dangerous Method Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1093
- **ZDI-CAN:** ZDI-CAN-17527
- **Date:** 2022-08-18
- **CVE:** CVE-2022-37365
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** PDF-XChange
- **Affected Products:** PDF-XChange Editor
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1093/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of PDF-XChange Editor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the saveAs method. The application exposes a JavaScript interface that allows the attacker to write arbitrary files. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

PDF-XChange has issued an update to correct this vulnerability. More details can be found at: https://www.tracker-software.com/product/pdf-xchange-editor/history

## Disclosure Timeline

- 2022-06-17 - Vulnerability reported to vendor
- 2022-08-18 - Coordinated public release of advisory
